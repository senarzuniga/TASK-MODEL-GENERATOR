"""Tests for the Task Model Generator."""

import io
from pathlib import Path

import pytest

from app.models import TaskModel, TaskStep, Priority, Status
from app.generator import WorkbookGenerator
from app.utils import export_to_dict, load_from_dict, sample_task_models


# ── Fixtures ──────────────────────────────────────────────────────────────────

@pytest.fixture
def simple_model() -> TaskModel:
    return TaskModel(
        id="TEST-001",
        name="Test Model",
        description="A test task model.",
        category="Testing",
        priority=Priority.HIGH,
        status=Status.PENDING,
        owner="Tester",
        steps=[
            TaskStep(order=1, name="Step A", assignee="Alice", estimated_hours=1.0),
            TaskStep(order=2, name="Step B", assignee="Bob", estimated_hours=2.5),
        ],
    )


@pytest.fixture
def models_list(simple_model: TaskModel) -> list:
    return [simple_model] + sample_task_models()


# ── Model tests ───────────────────────────────────────────────────────────────

class TestTaskStep:
    def test_default_status(self):
        step = TaskStep(order=1, name="My Step")
        assert step.status == Status.PENDING.value

    def test_invalid_order(self):
        with pytest.raises(Exception):
            TaskStep(order=0, name="Bad order")


class TestTaskModel:
    def test_total_hours(self, simple_model: TaskModel):
        assert simple_model.total_estimated_hours == 3.5

    def test_step_count(self, simple_model: TaskModel):
        assert simple_model.step_count == 2

    def test_default_priority(self):
        m = TaskModel(id="X", name="X")
        assert m.priority == Priority.MEDIUM.value

    def test_empty_steps_hours(self):
        m = TaskModel(id="X", name="X")
        assert m.total_estimated_hours == 0.0


# ── Serialisation tests ───────────────────────────────────────────────────────

class TestSerialization:
    def test_round_trip(self, models_list: list):
        exported = export_to_dict(models_list)
        restored = load_from_dict(exported)
        assert len(restored) == len(models_list)
        for original, restored_model in zip(models_list, restored):
            assert original.id == restored_model.id
            assert original.name == restored_model.name
            assert len(original.steps) == len(restored_model.steps)


# ── Generator tests ───────────────────────────────────────────────────────────

class TestWorkbookGenerator:
    def test_generates_file(self, tmp_path: Path, models_list: list):
        out = tmp_path / "test_output.xlsx"
        generator = WorkbookGenerator(models_list)
        result = generator.generate(out)
        assert result == out
        assert out.exists()
        assert out.stat().st_size > 0

    def test_generates_to_buffer(self, models_list: list):
        buf = io.BytesIO()
        WorkbookGenerator(models_list).generate(buf)
        buf.seek(0)
        assert len(buf.read()) > 0

    def test_summary_sheet_exists(self, tmp_path: Path, models_list: list):
        import openpyxl
        out = tmp_path / "out.xlsx"
        WorkbookGenerator(models_list).generate(out)
        wb = openpyxl.load_workbook(out)
        assert "Summary" in wb.sheetnames

    def test_model_sheets_created(self, tmp_path: Path, models_list: list):
        import openpyxl
        out = tmp_path / "out.xlsx"
        WorkbookGenerator(models_list).generate(out)
        wb = openpyxl.load_workbook(out)
        for model in models_list:
            assert model.name[:31] in wb.sheetnames

    def test_empty_models_list(self, tmp_path: Path):
        out = tmp_path / "empty.xlsx"
        WorkbookGenerator([]).generate(out)
        assert out.exists()
