"""
B2B Commercial Task Model Generator.

Generates a professionally formatted Excel workbook containing a structured
B2B sales task model with Execution Discipline, CRM Integration, AI-Ready
structure, and Maturity-Based Selling Model support.
"""

from .builder import build_workbook
from .models import Task, AutomationLevel, MaturityLevel, Priority

__all__ = [
    "build_workbook",
    "Task",
    "AutomationLevel",
    "MaturityLevel",
    "Priority",
]
