
"""
Entry point for the B2B Commercial Task Model Generator.

Usage
-----
    python main.py [--output PATH]

Examples
--------
    python main.py
    python main.py --output /reports/Sales_Tasks_Q1.xlsx
"""

from __future__ import annotations

import argparse
import sys
import logging

from generator import build_workbook


logging.basicConfig(
    filename='app.log',
    filemode='a',
    format='%(asctime)s - %(levelname)s - %(message)s',
    level=logging.ERROR
)


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Generate the Elite B2B Sales Task Model Excel workbook.\n\n"
            "The workbook contains:\n"
            "  • B2B Task Model  — full commercial execution task catalogue\n"
            "  • KPI Reference   — definitions and benchmarks for every KPI\n"
            "  • Legend & Guide  — colour coding and column explanations"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    parser.add_argument(
        "--output",
        "-o",
        default="Elite_B2B_Sales_Task_Model.xlsx",
        metavar="PATH",
        help=(
            "Destination file path for the generated .xlsx file. "
            "Defaults to 'Elite_B2B_Sales_Task_Model.xlsx' in the current directory."
        ),
    )
    return parser.parse_args(argv)


def main(argv: list[str] | None = None) -> int:
    args = parse_args(argv)
    try:
        saved_path = build_workbook(args.output)
        print(f"✅  Workbook created: {saved_path}")
        return 0
    except Exception as exc:  # noqa: BLE001
        logging.error("Error generating workbook", exc_info=True)
        print("❌  An error occurred while generating the workbook. Please check the logs for more details.", file=sys.stderr)
        return 1


if __name__ == "__main__":
    sys.exit(main())
