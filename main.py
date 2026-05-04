
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
    except FileNotFoundError as exc:
        logging.error("File not found: %s", exc, exc_info=True)
        print("❌  The specified file path was not found. Please check the path and try again.", file=sys.stderr)
    except ValueError as exc:
        logging.error("Value error: %s", exc, exc_info=True)
        print("❌  An invalid value was encountered. Please check the input values and try again.", file=sys.stderr)
    except Exception as exc:
        logging.error("Unexpected error: %s", exc, exc_info=True)
        print("❌  An unexpected error occurred. Please check the logs for more details.", file=sys.stderr)
    return 1


if __name__ == "__main__":
    sys.exit(main())
