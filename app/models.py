"""Data models for the Task Model Generator."""

from __future__ import annotations

from enum import Enum
from typing import List, Optional
from pydantic import BaseModel, ConfigDict, Field


class Priority(str, Enum):
    LOW = "Low"
    MEDIUM = "Medium"
    HIGH = "High"
    CRITICAL = "Critical"


class Status(str, Enum):
    PENDING = "Pending"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"
    CANCELLED = "Cancelled"


class TaskStep(BaseModel):
    """A single step within a task model."""

    order: int = Field(..., ge=1, description="Step order number")
    name: str = Field(..., min_length=1, description="Step name")
    description: str = Field(default="", description="Step description")
    assignee: str = Field(default="", description="Person responsible for this step")
    estimated_hours: float = Field(default=0.0, ge=0, description="Estimated hours")
    status: Status = Field(default=Status.PENDING)

    model_config = ConfigDict(use_enum_values=True)


class TaskModel(BaseModel):
    """A complete task model with metadata and steps."""

    id: str = Field(..., min_length=1, description="Unique task model identifier")
    name: str = Field(..., min_length=1, description="Task model name")
    description: str = Field(default="", description="Task model description")
    category: str = Field(default="General", description="Task category")
    priority: Priority = Field(default=Priority.MEDIUM)
    status: Status = Field(default=Status.PENDING)
    owner: str = Field(default="", description="Task model owner")
    steps: List[TaskStep] = Field(default_factory=list)

    model_config = ConfigDict(use_enum_values=True)

    @property
    def total_estimated_hours(self) -> float:
        return sum(step.estimated_hours for step in self.steps)

    @property
    def step_count(self) -> int:
        return len(self.steps)
