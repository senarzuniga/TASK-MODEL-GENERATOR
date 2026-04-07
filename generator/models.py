"""
Data models for the B2B Commercial Task Model.

Each Task captures the full execution discipline required to eliminate
random sales behaviour and support AI / CRM integration.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from enum import Enum



class AutomationLevel(str, Enum):
    """Degree of process automation achievable for a given task."""

    MANUAL = "Manual"
    SEMI = "Semi"
    FULL = "Full"


class MaturityLevel(str, Enum):
    """Sales-organisation maturity tier required to execute the task."""

    BASIC = "Basic"
    ADVANCED = "Advanced"
    ELITE = "Elite"


class Priority(str, Enum):
    """Execution priority of the task."""

    HIGH = "High"
    MEDIUM = "Medium"
    LOW = "Low"


@dataclass
class Task:
    """
    Single unit of commercial execution discipline.

    Attributes
    ----------
    domain:
        High-level commercial domain (e.g. "Pipeline Management", "KAM").
    name:
        Short, descriptive task name.
    objective:
        What outcome the task is designed to achieve.
    trigger:
        The event or time condition that initiates the task.
    method:
        Step-by-step description of how the task is executed.
    inputs:
        Data or resources required before execution.
    output:
        Tangible deliverable produced by the task.
    primary_kpi:
        Main KPI that the task moves.
    secondary_kpis:
        Supporting metrics affected by the task.
    frequency:
        How often the task should be performed.
    priority:
        Execution priority level.
    owner:
        Role responsible for executing the task.
    dependencies:
        Pre-conditions or other tasks this task depends on.
    tools:
        Systems, templates, or documents needed.
    ai_role:
        How an AI agent can augment or automate the task.
    automation_level:
        Current or target automation classification.
    maturity_level:
        Minimum sales-organisation maturity required.
    """

    domain: str
    name: str
    objective: str
    trigger: str
    method: str
    inputs: str
    output: str
    primary_kpi: str
    secondary_kpis: str
    frequency: str
    priority: Priority
    owner: str
    dependencies: str
    tools: str
    ai_role: str
    automation_level: AutomationLevel
    maturity_level: MaturityLevel

    def to_row(self) -> list[str]:
        """Return the task as a flat list suitable for an Excel row."""
        return [
            self.domain,
            self.name,
            self.objective,
            self.trigger,
            self.method,
            self.inputs,
            self.output,
            self.primary_kpi,
            self.secondary_kpis,
            self.frequency,
            self.priority.value,
            self.owner,
            self.dependencies,
            self.tools,
            self.ai_role,
            self.automation_level.value,
            self.maturity_level.value,
        ]

    @staticmethod
    def headers() -> list[str]:
        """Return the canonical column headers for the task model sheet."""
        return [
            "Domain",
            "Task Name",
            "Objective",
            "Trigger (When to Execute)",
            "Execution Method (How)",
            "Key Inputs Required",
            "Expected Output",
            "Primary KPI Impacted",
            "Secondary KPIs",
            "Frequency",
            "Priority Level",
            "Owner Role",
            "Dependencies",
            "Tools / Documents Required",
            "AI Augmentation Role",
            "Automation Level",
            "Sales Maturity Level",
        ]
