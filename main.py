"""Command-line entry point – generates an Excel workbook from sample models."""

from __future__ import annotations

import sys
from pathlib import Path

from app import WorkbookGenerator
from app.utils import sample_task_models


def main(output_path: str = "output/task_models.xlsx") -> None:
    models = sample_task_models()
    generator = WorkbookGenerator(models)
    result = generator.generate(output_path)
    print(f"Workbook generated: {result.resolve()}")


if __name__ == "__main__":
    path = sys.argv[1] if len(sys.argv) > 1 else "output/task_models.xlsx"
    main(path)
