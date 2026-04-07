"""
B2B sales task catalogue.

Each task is an instance of :class:`~generator.models.Task` and follows the
four-pillar framework:

1. **Execution Discipline** – every task has a Trigger, Method, and Output.
2. **Scalable CRM Integration** – each row maps directly to a CRM workflow,
   AI-agent trigger, or dashboard KPI.
3. **AI-Ready Structure** – the AI Augmentation Role field specifies where an
   agent can plug in (scoring, next-best-action, forecasting, risk).
4. **Maturity-Based Selling** – Basic → Advanced → Elite progression.
"""

from .models import AutomationLevel, MaturityLevel, Priority, Task

# ---------------------------------------------------------------------------
# Helper alias for brevity
# ---------------------------------------------------------------------------
M = AutomationLevel
L = MaturityLevel
P = Priority


TASKS: list[Task] = [

    # ======================================================================
    # DOMAIN: PIPELINE & OPPORTUNITY MANAGEMENT
    # ======================================================================

    Task(
        domain="Pipeline Management",
        name="Weekly Pipeline Deep Review",
        objective="Ensure all opportunities are progressing with clear next steps",
        trigger="Weekly fixed cadence (e.g. every Monday morning)",
        method=(
            "Review every open deal: validate stage, next action, decision maker, "
            "and probability; remove or quarantine stalled / dead deals"
        ),
        inputs="CRM pipeline snapshot, last-activity log, opportunity status",
        output="Clean pipeline with updated stages and a realistic forecast",
        primary_kpi="Forecast Accuracy",
        secondary_kpis="Conversion Rate, Sales Cycle Length",
        frequency="Weekly",
        priority=P.HIGH,
        owner="Sales Manager",
        dependencies="CRM hygiene discipline",
        tools="Pipeline dashboard, CRM report",
        ai_role="Highlight stalled deals, recommend next actions automatically",
        automation_level=M.SEMI,
        maturity_level=L.ADVANCED,
    ),

    Task(
        domain="Pipeline Management",
        name="Opportunity Qualification (Strict)",
        objective="Focus resources only on high-value, winnable deals",
        trigger="At opportunity creation or first qualification call",
        method=(
            "Apply structured qualification framework (BANT or MEDDICC); "
            "score fit vs ideal customer profile; disqualify weak deals early"
        ),
        inputs="Opportunity data, customer need statement, budget signal",
        output="Qualified / Disqualified decision with documented rationale",
        primary_kpi="Win Rate",
        secondary_kpis="Sales Efficiency, Pipeline Coverage",
        frequency="Per opportunity",
        priority=P.HIGH,
        owner="Sales Representative",
        dependencies="Lead quality, ICP definition",
        tools="Qualification checklist, CRM opportunity form",
        ai_role="Score opportunity win-probability; flag missing qualification criteria",
        automation_level=M.SEMI,
        maturity_level=L.ELITE,
    ),

    Task(
        domain="Pipeline Management",
        name="Deal Acceleration Plan",
        objective="Reduce time-to-close for deals exceeding expected cycle length",
        trigger="Deal age > defined cycle threshold or manual flag",
        method=(
            "Identify blockers (technical, commercial, political); define "
            "a time-boxed action plan with owners and deadlines; escalate if needed"
        ),
        inputs="Deal timeline, stakeholder map, outstanding objections",
        output="Recovery plan with specific actions and target close date",
        primary_kpi="Sales Cycle Length",
        secondary_kpis="Win Rate, Forecast Accuracy",
        frequency="Ad-hoc (triggered)",
        priority=P.HIGH,
        owner="Sales Representative",
        dependencies="Stakeholder access, management support",
        tools="Deal review template, CRM timeline view",
        ai_role="Detect delay patterns; suggest proven acceleration tactics",
        automation_level=M.SEMI,
        maturity_level=L.ELITE,
    ),

    Task(
        domain="Pipeline Management",
        name="Pipeline Coverage Monitoring",
        objective="Maintain sufficient pipeline to hit revenue targets",
        trigger="Monthly pipeline review or when coverage ratio drops below 3×",
        method=(
            "Calculate pipeline-to-quota coverage per rep and team; "
            "identify gaps; trigger prospecting campaigns if under 3× coverage"
        ),
        inputs="Open pipeline value, quota, historical conversion rates",
        output="Coverage ratio report with gap analysis and action items",
        primary_kpi="Pipeline Coverage Ratio",
        secondary_kpis="Revenue Attainment, Forecast Accuracy",
        frequency="Monthly",
        priority=P.HIGH,
        owner="Sales Manager",
        dependencies="Accurate CRM data",
        tools="CRM analytics, pipeline health dashboard",
        ai_role="Predict end-of-quarter attainment; auto-trigger prospecting alerts",
        automation_level=M.FULL,
        maturity_level=L.ADVANCED,
    ),

    # ======================================================================
    # DOMAIN: KEY ACCOUNT MANAGEMENT (KAM)
    # ======================================================================

    Task(
        domain="KAM",
        name="Top Account Strategic Plan",
        objective="Maximise long-term value from key accounts",
        trigger="Quarterly planning cycle",
        method=(
            "Define growth plan: cross-sell / upsell opportunities, stakeholder "
            "engagement roadmap, competitive risks, and success metrics"
        ),
        inputs="Customer revenue history, product-usage data, org chart",
        output="Account growth roadmap (12-month horizon)",
        primary_kpi="Account Revenue Growth",
        secondary_kpis="Customer Retention, Gross Margin",
        frequency="Quarterly",
        priority=P.HIGH,
        owner="Key Account Manager",
        dependencies="Data availability, executive sponsorship",
        tools="Account plan template, CRM account view",
        ai_role="Surface cross-sell opportunities from usage and contract data",
        automation_level=M.SEMI,
        maturity_level=L.ELITE,
    ),

    Task(
        domain="KAM",
        name="Stakeholder Power Mapping",
        objective="Understand and navigate decision dynamics within key accounts",
        trigger="Quarterly account review or new opportunity identified",
        method=(
            "Map all stakeholders: role, influence level, attitude (champion/neutral/"
            "blocker), and engagement status; identify white-space contacts"
        ),
        inputs="Customer org chart, meeting notes, LinkedIn intel",
        output="Stakeholder map with engagement strategy per contact",
        primary_kpi="Win Rate",
        secondary_kpis="Deal Velocity, Relationship Depth Score",
        frequency="Quarterly",
        priority=P.HIGH,
        owner="Key Account Manager",
        dependencies="Customer access, org data availability",
        tools="Stakeholder mapping tool, CRM contacts module",
        ai_role="Identify missing stakeholders; flag relationship gaps vs competitors",
        automation_level=M.SEMI,
        maturity_level=L.ADVANCED,
    ),

    Task(
        domain="KAM",
        name="Executive Relationship Plan",
        objective="Build and maintain top-level trust in strategic accounts",
        trigger="Quarterly — for accounts above defined revenue threshold",
        method=(
            "Define executive touchpoint calendar: business reviews, industry events, "
            "advisory sessions; align internal executive sponsor"
        ),
        inputs="Account importance score, customer hierarchy, last exec interaction",
        output="Executive engagement calendar with topics and owners",
        primary_kpi="Customer Retention",
        secondary_kpis="Strategic Deal Volume, NPS",
        frequency="Quarterly",
        priority=P.HIGH,
        owner="Sales Director",
        dependencies="Access to customer executives, internal executive sponsor",
        tools="Engagement plan template, calendar integration",
        ai_role="Suggest optimal timing and personalised discussion topics",
        automation_level=M.MANUAL,
        maturity_level=L.ELITE,
    ),

    Task(
        domain="KAM",
        name="Account Health Score Review",
        objective="Detect at-risk accounts before churn occurs",
        trigger="Monthly or when health-score alert fires",
        method=(
            "Review composite health score (usage, support tickets, NPS, engagement, "
            "commercial signals); agree remediation actions if score is amber/red"
        ),
        inputs="Product usage data, support history, NPS, commercial calendar",
        output="Health score per account with red/amber/green classification",
        primary_kpi="Customer Retention",
        secondary_kpis="Churn Rate, Net Revenue Retention",
        frequency="Monthly",
        priority=P.HIGH,
        owner="Key Account Manager",
        dependencies="Integrated data sources, health model definition",
        tools="Customer health dashboard, CRM",
        ai_role="Predict churn probability; auto-alert KAM when score drops",
        automation_level=M.FULL,
        maturity_level=L.ELITE,
    ),

    # ======================================================================
    # DOMAIN: CUSTOMER GROWTH
    # ======================================================================

    Task(
        domain="Customer Growth",
        name="Installed-Base Opportunity Scan",
        objective="Identify hidden revenue in existing customers",
        trigger="Monthly — run across full installed base",
        method=(
            "Analyse product penetration vs addressable potential; compare "
            "each customer's current footprint against portfolio capacity"
        ),
        inputs="Installed base data, full product portfolio, customer segment",
        output="Prioritised list of upsell / cross-sell opportunities",
        primary_kpi="Upsell Revenue",
        secondary_kpis="Customer Lifetime Value, Wallet Share",
        frequency="Monthly",
        priority=P.HIGH,
        owner="Sales Representative",
        dependencies="Data quality, accurate installed-base records",
        tools="CRM analytics, product catalogue",
        ai_role="Detect penetration gaps and recommend next-best product",
        automation_level=M.FULL,
        maturity_level=L.ELITE,
    ),

    Task(
        domain="Customer Growth",
        name="Cross-Sell Campaign Execution",
        objective="Increase product adoption within existing customer base",
        trigger="Monthly campaign cycle or trigger from opportunity scan",
        method=(
            "Segment customers by fit score; design tailored value proposition; "
            "execute multi-touch outreach; measure conversion"
        ),
        inputs="Customer segmentation, product fit scores, campaign brief",
        output="Campaign results: contacts reached, meetings booked, pipeline created",
        primary_kpi="Revenue Growth",
        secondary_kpis="Conversion Rate, Campaign ROI",
        frequency="Monthly",
        priority=P.HIGH,
        owner="Marketing + Sales",
        dependencies="Segmentation quality, content availability",
        tools="Marketing automation, CRM campaign module, email templates",
        ai_role="Optimise audience targeting; personalise messaging at scale",
        automation_level=M.FULL,
        maturity_level=L.ADVANCED,
    ),

    Task(
        domain="Customer Growth",
        name="Customer Value Review (QBR)",
        objective="Demonstrate ROI delivered; strengthen relationship and identify growth",
        trigger="Quarterly — scheduled with key accounts and high-potential customers",
        method=(
            "Prepare data-driven report: achievements vs objectives, ROI, product "
            "roadmap alignment, agreed actions for next quarter"
        ),
        inputs="Customer KPI data, product usage, support metrics, agreed goals",
        output="Executive value presentation and agreed next-quarter action plan",
        primary_kpi="Customer Retention",
        secondary_kpis="Upsell Pipeline, NPS",
        frequency="Quarterly",
        priority=P.HIGH,
        owner="Key Account Manager",
        dependencies="Data availability from customer and internal sources",
        tools="QBR presentation template, analytics dashboard",
        ai_role="Auto-generate insights, anomaly commentary, and next-step suggestions",
        automation_level=M.SEMI,
        maturity_level=L.ELITE,
    ),

    # ======================================================================
    # DOMAIN: SALES EXECUTION
    # ======================================================================

    Task(
        domain="Sales Execution",
        name="Next-Best-Action Planning",
        objective="Ensure every account and opportunity has a defined, high-impact next step",
        trigger="Weekly — start of each working week",
        method=(
            "Review account portfolio; assess current status; define single most "
            "impactful action per account; schedule it in CRM"
        ),
        inputs="Account status, open opportunities, activity log",
        output="Prioritised action list with owners and due dates",
        primary_kpi="Sales Productivity",
        secondary_kpis="Pipeline Health, Activity Coverage",
        frequency="Weekly",
        priority=P.HIGH,
        owner="Sales Representative",
        dependencies="CRM accuracy, up-to-date opportunity data",
        tools="Task planner, CRM activity module",
        ai_role="Recommend highest-ROI actions based on deal stage and account signals",
        automation_level=M.FULL,
        maturity_level=L.ELITE,
    ),

    Task(
        domain="Sales Execution",
        name="Customer Follow-Up Discipline",
        objective="Eliminate lost opportunities caused by lack of timely follow-up",
        trigger="After every customer interaction (call, meeting, email)",
        method=(
            "Log interaction summary in CRM within 24 hours; define and schedule "
            "concrete next step; set reminders"
        ),
        inputs="Meeting or call notes, agreed actions",
        output="Updated CRM record with logged interaction and next-step task",
        primary_kpi="Conversion Rate",
        secondary_kpis="Customer Engagement Score, Response Rate",
        frequency="Continuous",
        priority=P.HIGH,
        owner="Sales Representative",
        dependencies="CRM discipline, rep training",
        tools="CRM, email integration, meeting-note templates",
        ai_role="Auto-transcribe meetings; suggest follow-up draft; flag overdue tasks",
        automation_level=M.SEMI,
        maturity_level=L.ADVANCED,
    ),

    Task(
        domain="Sales Execution",
        name="Proposal Optimisation",
        objective="Increase proposal win rate through customer-centric design",
        trigger="Before sending any commercial proposal",
        method=(
            "Align proposal structure to customer pain points, value drivers, "
            "and decision criteria; validate pricing; include ROI calculation"
        ),
        inputs="Customer needs assessment, pricing matrix, competition intel",
        output="Tailored, value-focused proposal ready for submission",
        primary_kpi="Win Rate",
        secondary_kpis="Average Deal Size, Proposal-to-Close Ratio",
        frequency="Per opportunity",
        priority=P.HIGH,
        owner="Sales Representative",
        dependencies="Deep customer understanding, approved pricing",
        tools="Proposal templates, ROI calculator, CPQ tool",
        ai_role="Draft personalised proposal narrative; suggest pricing tier",
        automation_level=M.SEMI,
        maturity_level=L.ELITE,
    ),

    Task(
        domain="Sales Execution",
        name="Competitive Displacement Planning",
        objective="Win business from competitors in target accounts",
        trigger="When competitive threat is identified in an account",
        method=(
            "Map competitor's current footprint; identify dissatisfaction signals; "
            "build business case for switching; define phased displacement approach"
        ),
        inputs="Competitive intel, customer pain points, switching-cost analysis",
        output="Competitive displacement playbook for the account",
        primary_kpi="Win Rate",
        secondary_kpis="New Logo Revenue, Market Share",
        frequency="Per opportunity",
        priority=P.HIGH,
        owner="Sales Representative",
        dependencies="Competitive intelligence, executive access",
        tools="Battlecard library, displacement playbook template",
        ai_role="Monitor competitor signals; surface vulnerable accounts",
        automation_level=M.SEMI,
        maturity_level=L.ELITE,
    ),

    # ======================================================================
    # DOMAIN: AFTER SALES
    # ======================================================================

    Task(
        domain="After Sales",
        name="Service Opportunity Identification",
        objective="Generate incremental revenue from the installed base post-sale",
        trigger="Monthly — automated scan of service eligibility",
        method=(
            "Analyse usage data for equipment age, service gaps, upgrade eligibility; "
            "produce prioritised call list for service team"
        ),
        inputs="Installed-base data, service contract status, usage metrics",
        output="Prioritised service opportunity list with revenue potential",
        primary_kpi="Service Revenue",
        secondary_kpis="Customer Retention, Gross Margin",
        frequency="Monthly",
        priority=P.HIGH,
        owner="Service Sales",
        dependencies="Data quality, accurate installed-base records",
        tools="Service analytics dashboard, CRM",
        ai_role="Predict service needs before failure; score urgency",
        automation_level=M.FULL,
        maturity_level=L.ELITE,
    ),

    Task(
        domain="After Sales",
        name="Renewal Risk Detection",
        objective="Prevent contract churn through early risk identification",
        trigger="90 / 60 / 30 days before contract expiration, or health-score alert",
        method=(
            "Flag low-engagement or dissatisfied customers; investigate root cause; "
            "activate retention plan; escalate when needed"
        ),
        inputs="Usage data, support ticket volume, NPS, last executive interaction",
        output="Risk-flagged account list with remediation actions",
        primary_kpi="Customer Retention",
        secondary_kpis="Net Revenue Retention, Churn Rate",
        frequency="Monthly (continuous monitoring)",
        priority=P.HIGH,
        owner="Key Account Manager",
        dependencies="Integrated customer data, health model",
        tools="Customer health dashboard, renewal playbook",
        ai_role="Predict churn probability; recommend intervention timing and message",
        automation_level=M.FULL,
        maturity_level=L.ELITE,
    ),

    Task(
        domain="After Sales",
        name="Post-Implementation Success Review",
        objective="Validate that delivered solution meets agreed success criteria",
        trigger="30 / 90 days after go-live",
        method=(
            "Conduct structured review with customer: measure KPIs vs baseline, "
            "address adoption gaps, document testimonial / case-study data"
        ),
        inputs="Implementation plan, agreed success metrics, usage data",
        output="Success review report; testimonial asset; next-step action plan",
        primary_kpi="Customer Satisfaction (CSAT)",
        secondary_kpis="Upsell Pipeline, Reference Customer Rate",
        frequency="Per project",
        priority=P.MEDIUM,
        owner="Customer Success / KAM",
        dependencies="Implementation completion, data availability",
        tools="Success review template, analytics dashboard",
        ai_role="Auto-generate performance summary and comparison vs benchmark",
        automation_level=M.SEMI,
        maturity_level=L.ADVANCED,
    ),

    # ======================================================================
    # DOMAIN: STRATEGY & PERFORMANCE
    # ======================================================================

    Task(
        domain="Strategy & Performance",
        name="Sales vs Plan Analysis",
        objective="Track and explain performance vs revenue targets",
        trigger="Monthly — first week of the new month",
        method=(
            "Compare actual sales vs budget and prior year; decompose variance "
            "by team, product, region; define corrective actions"
        ),
        inputs="Actual sales data, budget plan, prior-year baseline",
        output="Gap analysis with root-cause commentary and action items",
        primary_kpi="Revenue Attainment",
        secondary_kpis="Forecast Accuracy, Growth Rate",
        frequency="Monthly",
        priority=P.HIGH,
        owner="Sales Management",
        dependencies="Timely and accurate sales data",
        tools="BI dashboard, management report template",
        ai_role="Explain deviations in natural language; predict end-of-period outcome",
        automation_level=M.FULL,
        maturity_level=L.ADVANCED,
    ),

    Task(
        domain="Strategy & Performance",
        name="Portfolio Risk Analysis (80/20)",
        objective="Identify revenue concentration risk and diversification opportunities",
        trigger="Quarterly",
        method=(
            "Run Pareto analysis on revenue by customer; classify risk tier; "
            "set diversification targets; adjust prospecting priorities"
        ),
        inputs="Revenue per customer, customer segment data",
        output="Risk classification report with diversification action plan",
        primary_kpi="Revenue Stability Index",
        secondary_kpis="Customer Concentration Ratio, New Logo Revenue",
        frequency="Quarterly",
        priority=P.HIGH,
        owner="Sales Management",
        dependencies="Clean customer revenue data",
        tools="Pareto analysis template, CRM analytics",
        ai_role="Auto-detect concentration risk; model diversification scenarios",
        automation_level=M.FULL,
        maturity_level=L.ADVANCED,
    ),

    Task(
        domain="Strategy & Performance",
        name="Market Intelligence Update",
        objective="Keep the commercial team informed of market shifts and opportunities",
        trigger="Monthly — standing agenda item in team meeting",
        method=(
            "Collect and synthesise: competitor moves, industry trends, regulatory "
            "changes, new customer segments; distribute as briefing"
        ),
        inputs="External reports, competitor news, customer feedback, analyst data",
        output="Market intelligence briefing (1-page summary + key actions)",
        primary_kpi="Strategic Alignment Score",
        secondary_kpis="Opportunity Creation Rate, Win Rate vs Competitor",
        frequency="Monthly",
        priority=P.MEDIUM,
        owner="Marketing",
        dependencies="Access to external data sources",
        tools="Intelligence reports, news aggregators, analyst subscriptions",
        ai_role="Summarise trends; flag competitor threats; generate briefing draft",
        automation_level=M.SEMI,
        maturity_level=L.ADVANCED,
    ),

    Task(
        domain="Strategy & Performance",
        name="Sales Capability Assessment",
        objective="Identify skills gaps and build a high-performance sales team",
        trigger="Semi-annual or following significant miss vs target",
        method=(
            "Assess each rep against defined competency framework; produce "
            "individual development plans; align coaching to gaps"
        ),
        inputs="Competency framework, performance data, manager observations",
        output="Individual capability scores and development roadmap",
        primary_kpi="Sales Productivity per Rep",
        secondary_kpis="Ramp Time, Win Rate",
        frequency="Semi-annual",
        priority=P.MEDIUM,
        owner="Sales Manager",
        dependencies="Competency framework, 360 input",
        tools="Skills assessment tool, coaching plan template",
        ai_role="Analyse call recordings and CRM data to identify skill gaps",
        automation_level=M.SEMI,
        maturity_level=L.ADVANCED,
    ),

    # ======================================================================
    # DOMAIN: PROSPECTING & LEAD GENERATION
    # ======================================================================

    Task(
        domain="Prospecting",
        name="Ideal Customer Profile (ICP) Refresh",
        objective="Keep targeting criteria aligned with market and portfolio evolution",
        trigger="Quarterly or when win-rate drops below threshold",
        method=(
            "Analyse closed-won data; identify common attributes of best customers; "
            "update ICP definition; align Marketing and Sales"
        ),
        inputs="Closed-won / lost data, customer firmographics, product-fit data",
        output="Updated ICP definition and target account criteria",
        primary_kpi="Lead-to-Opportunity Conversion",
        secondary_kpis="Win Rate, CAC",
        frequency="Quarterly",
        priority=P.MEDIUM,
        owner="Marketing + Sales",
        dependencies="Sufficient closed deal volume for analysis",
        tools="CRM analytics, ICP template",
        ai_role="Cluster won accounts; identify predictive ICP attributes",
        automation_level=M.SEMI,
        maturity_level=L.ADVANCED,
    ),

    Task(
        domain="Prospecting",
        name="Target Account List Management",
        objective="Maintain a focused, dynamic list of high-potential prospects",
        trigger="Monthly review",
        method=(
            "Score and rank prospect accounts vs ICP; activate top-tier accounts "
            "in outreach sequences; retire or deprioritise low-fit accounts"
        ),
        inputs="Prospect database, ICP criteria, engagement history",
        output="Tiered target account list (Tier 1 / 2 / 3)",
        primary_kpi="Pipeline Creation Rate",
        secondary_kpis="Outreach Efficiency, Lead Quality Score",
        frequency="Monthly",
        priority=P.HIGH,
        owner="Sales Development Representative",
        dependencies="ICP definition, prospect data quality",
        tools="CRM prospect module, intent data platform",
        ai_role="Score accounts with intent signals; auto-prioritise outreach",
        automation_level=M.FULL,
        maturity_level=L.ELITE,
    ),

    Task(
        domain="Prospecting",
        name="Outbound Prospecting Cadence",
        objective="Generate qualified meetings from target accounts",
        trigger="Weekly — ongoing execution per SDR",
        method=(
            "Execute multi-channel outreach sequence (email, phone, LinkedIn, video); "
            "personalise per account; track response and adjust"
        ),
        inputs="Target account list, contact data, value-proposition messaging",
        output="Qualified meetings booked; new opportunities created in CRM",
        primary_kpi="Meetings Booked",
        secondary_kpis="Reply Rate, Opportunity Creation Rate",
        frequency="Daily / Weekly",
        priority=P.HIGH,
        owner="Sales Development Representative",
        dependencies="Target account list, approved messaging, tools access",
        tools="Outreach / Salesloft, LinkedIn Sales Navigator, CRM",
        ai_role="Personalise outreach at scale; optimise send time and sequence steps",
        automation_level=M.SEMI,
        maturity_level=L.ADVANCED,
    ),
]
