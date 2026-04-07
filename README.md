# 📋 Task Model Generator

A Streamlit application that lets you **create, manage and export commercial task models** to Excel workbooks.

---

## ✨ Features

- Interactive UI to define task models (name, category, priority, owner, steps, estimated hours …)
- Per-step detail: assignee, description, estimated hours, status
- Summary dashboard with all models at a glance
- One-click Excel export with a styled **Summary** sheet and individual model sheets
- CLI entry-point for headless workbook generation
- VS Code launch profiles for Streamlit, CLI and pytest

---

## 🗂️ Repository structure

```
TASK-MODEL-GENERATOR/
├── app/
│   ├── __init__.py        # Public API
│   ├── models.py          # Pydantic data models (TaskModel, TaskStep, …)
│   ├── generator.py       # Excel workbook builder (openpyxl)
│   └── utils.py           # Serialisation helpers + sample data
├── tests/
│   └── test_generator.py  # pytest test suite
├── output/                # Generated workbooks (git-ignored)
├── .streamlit/
│   └── config.toml        # Streamlit theme
├── .vscode/
│   ├── extensions.json    # Recommended VS Code extensions
│   ├── launch.json        # Debug/run profiles
│   └── settings.json      # Workspace settings
├── streamlit_app.py       # Streamlit entry point
├── main.py                # CLI entry point
└── requirements.txt
```

---

## 🚀 Quick start

### 1 · Clone the repository

```bash
git clone https://github.com/senarzuniga/TASK-MODEL-GENERATOR.git
cd TASK-MODEL-GENERATOR
```

### 2 · Create a virtual environment

```bash
# macOS / Linux
python -m venv .venv
source .venv/bin/activate

# Windows (PowerShell)
python -m venv .venv
.venv\Scripts\Activate.ps1
```

### 3 · Install dependencies

```bash
pip install -r requirements.txt
```

### 4 · Run the Streamlit app

```bash
streamlit run streamlit_app.py
```

The app opens automatically at **http://localhost:8501**.

---

## 🖥️ VS Code

Open the repository folder in VS Code:

```bash
code .
```

VS Code will prompt you to install the **recommended extensions** (Python, debugpy, Black formatter …).  
Set the interpreter to `.venv/bin/python` (VS Code may detect it automatically).

Three **launch profiles** are available in the *Run & Debug* panel:

| Profile | What it does |
|---|---|
| **Streamlit App** | `streamlit run streamlit_app.py` with the debugger attached |
| **Generate Workbook (CLI)** | Runs `main.py` → writes `output/task_models.xlsx` |
| **Run Tests** | Executes the full pytest suite |

---

## ⚙️ CLI usage

Generate an Excel workbook from the built-in sample models:

```bash
python main.py                          # writes output/task_models.xlsx
python main.py path/to/my_output.xlsx  # custom path
```

---

## 🧪 Tests

```bash
python -m pytest tests/ -v
```

---

## 📦 Dependencies

| Package | Purpose |
|---|---|
| `streamlit` | Web UI |
| `openpyxl` | Excel workbook generation |
| `pandas` | DataFrame display in Streamlit |
| `pydantic` | Data validation & serialisation |
| `pytest` | Test runner |
