# FP&A Portfolio — Progress Log

## Phase 1 — Data Generation ✓ COMPLETE (March 16 2026)
- [x] Git and GitHub set up
- [x] VS Code installed
- [x] Repo created at github.com/Antoniojhm1/fpa-portfolio
- [x] Folder structure created: data/, sql/, notebooks/, powerbi/, portfolio/
- [x] README written and pushed
- [x] Synthetic data generated with Python (generate_data.py)
- [x] 5 CSV files created: customers, contracts, revenue_transactions, headcount, budget
- [x] All files pushed to GitHub

## Data summary — FORGE (fictional B2B SaaS company)
- 500 customers across Enterprise, Mid-Market, SMB segments
- 7,375 revenue transactions (Jan 2024 – Mar 2026)
- 42 employees across 5 departments
- 135 months of budget vs actual data
- Churn rates: Enterprise 2%, Mid-Market 8%, SMB 15%

## Phase 2 — SQL Database ✓ COMPLETE (March 17 2026)
- [x] Created SQLite database (forge.db) from 5 CSV files
- [x] Written SQL query library (queries.sql) with 7 core queries
- [x] Revenue by segment — Enterprise $14M, Mid-Market $8.4M, SMB $2.3M
- [x] Total ARR — $18.8M across 500 customers
- [x] Budget vs actual — all departments over budget, G&A worst at +5.5%
- [x] JOIN queries connecting customers, contracts, revenue tables

## Phase 3 — Python Modeling ✓ COMPLETE (March 18 2026)
- [x] Jupyter notebook setup complete
- [x] Notebook 1: Revenue forecast complete
  - Historical trend analysis Jan 2024 – Mar 2026
  - 6-month forward forecast (Apr–Sep 2026)
  - Trend slope: -$3,797/month (plateau phase)
  - Charts saved: revenue_trend.png, revenue_forecast.png
- [x] Notebook 2: Cohort retention analysis complete
  - Monthly cohort construction by first transaction month (27 cohorts)
  - Retention matrix: cohort × months 0–12
  - Retention heatmap, segment curves (Enterprise/Mid-Market/SMB), overall blended curve
  - Charts saved: cohort_heatmap.png, cohort_retention_curves.png, cohort_avg_retention.png
- [x] Notebook 3: Variance engine complete
  - Budget vs actual by department, ±10% materiality flagging
  - Bar chart, avg monthly variance % horizontal bar chart, variance heatmap
  - Charts saved: variance_by_dept.png, variance_avg_by_dept.png, variance_heatmap.png
- [x] Notebook 4: Scenario analysis complete
  - Upside: $1.54M MRR | Base: $0.98M MRR | Downside: $0.50M MRR
  - Upside-to-Downside gap: $12.5M annualized
  - Chart saved: scenario_analysis.png

## Phase 4 — Power BI Dashboard ✓ COMPLETE (March 30 2026)
- [x] Connected Power BI to SQLite (forge.db) — 5 tables loaded
- [x] Built 4 KPI cards: Total ARR, MRR, Active Customers, Avg MRR per Customer
- [x] Built 3 charts: Revenue by Segment, Budget vs Actual by Department, Cohort Retention
- [x] Dashboard file saved: forge_dashboard.pbix

## Phase 5 — Portfolio HTML Page (NEXT)
- [ ] Build public portfolio page
- [ ] Deploy via GitHub Pages