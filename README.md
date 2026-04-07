# TASK-MODEL-GENERATOR — Elite B2B Sales Task Model

A Python code generator that produces a **professionally formatted Excel workbook** containing a complete B2B commercial execution framework.

---

## Why This Exists

Random sales behaviour kills revenue. This generator enforces four pillars of commercial excellence:

| Pillar | What It Solves |
|---|---|
| **Execution Discipline** | Every task has a Trigger, Method, and Output — no ambiguity |
| **Scalable CRM Integration** | Each row maps to a CRM workflow, AI agent trigger, or dashboard KPI |
| **AI-Ready Structure** | AI Augmentation Role field specifies exactly where agents plug in |
| **Maturity-Based Selling** | Basic → Advanced → Elite progression adapts to your organisation |

---

## Generated Workbook

Running the generator produces `Elite_B2B_Sales_Task_Model.xlsx` with three sheets:

### Sheet 1 — B2B Task Model
The core task catalogue covering **7 commercial domains** and **25 tasks**, each with 17 structured columns:

| Column | Purpose |
|---|---|
| Domain | High-level commercial category |
| Task Name | Short descriptive name |
| Objective | Desired outcome |
| Trigger (When to Execute) | Time or event that starts the task |
| Execution Method (How) | Step-by-step execution instructions |
| Key Inputs Required | Data and resources needed |
| Expected Output | Tangible deliverable produced |
| Primary KPI Impacted | Main metric moved by this task |
| Secondary KPIs | Supporting metrics affected |
| Frequency | How often to execute |
| Priority Level | High / Medium / Low (colour-coded) |
| Owner Role | Who is accountable |
| Dependencies | Pre-conditions required |
| Tools / Documents Required | Systems and templates needed |
| AI Augmentation Role | How AI agents can support or automate |
| Automation Level | Manual / Semi / Full |
| Sales Maturity Level | Basic / Advanced / Elite (colour-coded) |

**Domains covered:**
- Pipeline Management
- Key Account Management (KAM)
- Customer Growth
- Sales Execution
- After Sales
- Strategy & Performance
- Prospecting

### Sheet 2 — KPI Reference
Definitions, measurement formulas, and target benchmarks for every KPI referenced in the task model.

### Sheet 3 — Legend & Guide
Colour coding explanations and full column guide for onboarding users and interpreting the workbook.

---

## Getting Started

### Requirements
- Python 3.9+
- openpyxl 3.1+

### Installation

```bash
pip install -r requirements.txt
```

### Usage

```bash
# Generate with default output path
python main.py

# Specify a custom output path
python main.py --output /path/to/Sales_Tasks_Q2.xlsx
python main.py -o Reports/Sales_Q1_2025.xlsx
```

### Output

```
✅  Workbook created: Elite_B2B_Sales_Task_Model.xlsx
```

---

## Project Structure

```
TASK-MODEL-GENERATOR/
├── main.py                   # CLI entry point
├── requirements.txt
├── generator/
│   ├── __init__.py           # Public API
│   ├── models.py             # Task dataclass + enums
│   ├── data.py               # Full task catalogue (25 tasks, 7 domains)
│   ├── formatter.py          # Excel styles, colours, column widths
│   └── builder.py            # Workbook assembly logic
└── tests/
    └── test_generator.py     # 24 automated tests
```

---

## Extending the Model

### Adding a new task
Edit `generator/data.py` and append a new `Task(...)` instance to the `TASKS` list:

```python
Task(
    domain="Your Domain",
    name="Task Name",
    objective="What outcome this achieves",
    trigger="When to execute",
    method="How to execute step by step",
    inputs="Required data and resources",
    output="Deliverable produced",
    primary_kpi="Main KPI",
    secondary_kpis="Other KPIs",
    frequency="Weekly",
    priority=Priority.HIGH,
    owner="Role Name",
    dependencies="Pre-conditions",
    tools="Tools and templates",
    ai_role="AI agent support description",
    automation_level=AutomationLevel.SEMI,
    maturity_level=MaturityLevel.ELITE,
)
```

### Adding a new domain
Tasks are automatically grouped by `domain` — simply use a new domain name in your `Task` instance.

---

## Running Tests

```bash
pip install pytest
python -m pytest tests/ -v
```

---

## Maturity Model

| Level | Description |
|---|---|
| **Basic** | Structure: define processes, roles, and accountability |
| **Advanced** | Optimisation: use data, KPIs, and tooling to improve |
| **Elite** | Predictive & AI-driven: automate, forecast, and scale |
