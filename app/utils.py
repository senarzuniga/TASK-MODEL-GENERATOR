"""Utility helpers for the Task Model Generator."""

from __future__ import annotations

from typing import Any, Dict, List

from .models import TaskModel, TaskStep


def export_to_dict(models: List[TaskModel]) -> List[Dict[str, Any]]:
    """Serialise a list of TaskModels to plain dictionaries."""
    return [m.model_dump() for m in models]


def load_from_dict(data: List[Dict[str, Any]]) -> List[TaskModel]:
    """Deserialise a list of plain dictionaries into TaskModel instances."""
    return [TaskModel(**item) for item in data]


def sample_task_models() -> List[TaskModel]:
    """Return a small set of sample TaskModels for demonstration purposes."""
    return [
        TaskModel(
            id="COMM-001",
            name="Sales Proposal",
            description="Standard commercial sales proposal workflow.",
            category="Sales",
            priority="High",
            status="Pending",
            owner="Alice Smith",
            steps=[
                TaskStep(order=1, name="Identify prospect", assignee="Alice Smith", estimated_hours=1.0),
                TaskStep(order=2, name="Qualify lead", assignee="Alice Smith", estimated_hours=2.0),
                TaskStep(order=3, name="Prepare proposal", description="Use approved template.", assignee="Alice Smith", estimated_hours=4.0),
                TaskStep(order=4, name="Internal review", assignee="Manager", estimated_hours=1.0),
                TaskStep(order=5, name="Send to client", assignee="Alice Smith", estimated_hours=0.5),
            ],
        ),
        TaskModel(
            id="COMM-002",
            name="Contract Negotiation",
            description="Handles the contract negotiation lifecycle.",
            category="Legal",
            priority="Critical",
            status="In Progress",
            owner="Bob Jones",
            steps=[
                TaskStep(order=1, name="Receive client terms", assignee="Bob Jones", estimated_hours=1.0),
                TaskStep(order=2, name="Legal review", assignee="Legal Team", estimated_hours=6.0),
                TaskStep(order=3, name="Counteroffer draft", assignee="Bob Jones", estimated_hours=3.0),
                TaskStep(order=4, name="Negotiation meeting", assignee="Bob Jones", estimated_hours=2.0),
                TaskStep(order=5, name="Sign & archive", assignee="Admin", estimated_hours=0.5),
            ],
        ),
        TaskModel(
            id="COMM-003",
            name="Invoice Processing",
            description="End-to-end invoice processing for commercial accounts.",
            category="Finance",
            priority="Medium",
            status="Pending",
            owner="Carol White",
            steps=[
                TaskStep(order=1, name="Receive invoice", assignee="Carol White", estimated_hours=0.25),
                TaskStep(order=2, name="Validate line items", assignee="Carol White", estimated_hours=1.0),
                TaskStep(order=3, name="Match PO", assignee="Carol White", estimated_hours=0.5),
                TaskStep(order=4, name="Approval", assignee="Finance Manager", estimated_hours=0.5),
                TaskStep(order=5, name="Payment execution", assignee="Accounts Payable", estimated_hours=0.25),
            ],
        ),
    ]
