"""Streamlit front-end for the Task Model Generator."""

from __future__ import annotations

import io
from typing import List

import pandas as pd
import streamlit as st

from app import TaskModel, TaskStep, WorkbookGenerator
from app.utils import sample_task_models

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Task Model Generator",
    page_icon="📋",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Session state bootstrap ───────────────────────────────────────────────────
if "models" not in st.session_state:
    st.session_state["models"]: List[TaskModel] = []

if "edit_index" not in st.session_state:
    st.session_state["edit_index"] = None


# ── Helpers ───────────────────────────────────────────────────────────────────
def get_models() -> List[TaskModel]:
    return st.session_state["models"]


def set_models(models: List[TaskModel]) -> None:
    st.session_state["models"] = models


def generate_workbook_bytes(models: List[TaskModel]) -> bytes:
    buf = io.BytesIO()
    WorkbookGenerator(models).generate(buf)
    buf.seek(0)
    return buf.read()


# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.title("📋 Task Model Generator")
    st.caption("Build, manage and export task models to Excel.")
    st.divider()

    if st.button("📦 Load sample models", use_container_width=True):
        set_models(sample_task_models())
        st.success("Sample models loaded!")

    if st.button("🗑️ Clear all models", use_container_width=True):
        set_models([])
        st.session_state["edit_index"] = None
        st.rerun()

    st.divider()
    models = get_models()
    if models:
        wb_bytes = generate_workbook_bytes(models)
        st.download_button(
            label="⬇️ Download Excel workbook",
            data=wb_bytes,
            file_name="task_models.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
            use_container_width=True,
        )
    else:
        st.info("Add at least one model to enable export.")


# ── Main area ─────────────────────────────────────────────────────────────────
st.header("Task Models")

models = get_models()

# Summary table
if models:
    summary = pd.DataFrame(
        [
            {
                "ID": m.id,
                "Name": m.name,
                "Category": m.category,
                "Priority": m.priority,
                "Status": m.status,
                "Owner": m.owner,
                "Steps": m.step_count,
                "Est. Hours": m.total_estimated_hours,
            }
            for m in models
        ]
    )
    st.dataframe(summary, use_container_width=True, hide_index=True)
else:
    st.info("No task models yet. Use the sidebar to load samples or add a new model below.")

st.divider()

# ── Add / Edit model form ─────────────────────────────────────────────────────
edit_index = st.session_state["edit_index"]
is_editing = edit_index is not None and 0 <= edit_index < len(models)
editing_model = models[edit_index] if is_editing else None

with st.expander("➕ Add / Edit Task Model", expanded=is_editing):
    with st.form("model_form", clear_on_submit=True):
        st.subheader("Model details")
        col1, col2 = st.columns(2)
        with col1:
            model_id = st.text_input("ID *", value=editing_model.id if editing_model else "")
            name = st.text_input("Name *", value=editing_model.name if editing_model else "")
            category = st.text_input("Category", value=editing_model.category if editing_model else "General")
            owner = st.text_input("Owner", value=editing_model.owner if editing_model else "")
        with col2:
            priority = st.selectbox(
                "Priority",
                ["Low", "Medium", "High", "Critical"],
                index=["Low", "Medium", "High", "Critical"].index(editing_model.priority) if editing_model else 1,
            )
            status = st.selectbox(
                "Status",
                ["Pending", "In Progress", "Completed", "Cancelled"],
                index=["Pending", "In Progress", "Completed", "Cancelled"].index(editing_model.status) if editing_model else 0,
            )
            description = st.text_area("Description", value=editing_model.description if editing_model else "", height=100)

        st.subheader("Steps")
        st.caption("Enter one step per row. At least one step is recommended.")

        default_steps = editing_model.steps if editing_model else []
        num_steps = st.number_input("Number of steps", min_value=1, max_value=20, value=max(len(default_steps), 1))

        steps: List[TaskStep] = []
        for i in range(int(num_steps)):
            existing = default_steps[i] if i < len(default_steps) else None
            with st.container():
                c1, c2, c3, c4, c5 = st.columns([1, 3, 4, 2, 2])
                step_name = c2.text_input(f"Name##{i}", value=existing.name if existing else "", placeholder="Step name")
                step_desc = c3.text_input(f"Description##{i}", value=existing.description if existing else "", placeholder="Optional description")
                step_assignee = c4.text_input(f"Assignee##{i}", value=existing.assignee if existing else "")
                step_hours = c5.number_input(f"Hours##{i}", min_value=0.0, step=0.25, value=existing.estimated_hours if existing else 0.0)
                if step_name:
                    steps.append(
                        TaskStep(
                            order=i + 1,
                            name=step_name,
                            description=step_desc,
                            assignee=step_assignee,
                            estimated_hours=step_hours,
                        )
                    )

        submitted = st.form_submit_button("💾 Save model", use_container_width=True)

    if submitted:
        if not model_id or not name:
            st.error("ID and Name are required fields.")
        elif not steps:
            st.error("Please provide at least one named step.")
        else:
            new_model = TaskModel(
                id=model_id,
                name=name,
                description=description,
                category=category,
                priority=priority,
                status=status,
                owner=owner,
                steps=steps,
            )
            current = list(get_models())
            if is_editing:
                current[edit_index] = new_model
                st.session_state["edit_index"] = None
            else:
                current.append(new_model)
            set_models(current)
            st.success(f"Model '{name}' saved!")
            st.rerun()

# ── Per-model detail & actions ────────────────────────────────────────────────
if models:
    st.divider()
    st.subheader("Model details")
    for idx, model in enumerate(models):
        with st.expander(f"📄 {model.id} – {model.name}"):
            col_a, col_b, col_c = st.columns([1, 1, 1])
            col_a.metric("Priority", model.priority)
            col_b.metric("Status", model.status)
            col_c.metric("Total Est. Hours", model.total_estimated_hours)

            if model.description:
                st.markdown(f"**Description:** {model.description}")

            if model.steps:
                step_df = pd.DataFrame(
                    [
                        {
                            "#": s.order,
                            "Step": s.name,
                            "Description": s.description,
                            "Assignee": s.assignee,
                            "Est. Hours": s.estimated_hours,
                            "Status": s.status,
                        }
                        for s in model.steps
                    ]
                )
                st.dataframe(step_df, use_container_width=True, hide_index=True)

            btn_col1, btn_col2 = st.columns(2)
            if btn_col1.button("✏️ Edit", key=f"edit_{idx}"):
                st.session_state["edit_index"] = idx
                st.rerun()
            if btn_col2.button("🗑️ Delete", key=f"del_{idx}"):
                current = list(get_models())
                current.pop(idx)
                set_models(current)
                if st.session_state["edit_index"] == idx:
                    st.session_state["edit_index"] = None
                st.rerun()
