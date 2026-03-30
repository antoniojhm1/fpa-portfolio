# FP&A Portfolio — Progress Log

## Phase 1 — Data Generation ✓ (March 16 2026)
Set up Git, GitHub, and VS Code. Created the project folder structure and generated synthetic data for FORGE — a fictional B2B SaaS company — using Python. 500 customers, 7,375 revenue transactions, 42 employees, 135 months of budget data. Churn rates set at 2% Enterprise, 8% Mid-Market, 15% SMB.

## Phase 2 — SQL Database ✓ (March 17 2026)
Loaded all CSV files into a SQLite database (forge.db). Wrote 7 core SQL queries covering revenue by segment, ARR breakdown, budget vs actual, and JOIN queries across multiple tables.

## Phase 3 — Python Modeling ✓ (March 2026)
Built 4 Jupyter notebooks:

**Notebook 1 — Revenue forecast:** historical trend analysis Jan 2024 to Mar 2026, 6-month forward projection. Revenue plateaued around $1.5M/month with a slight declining trend.

**Notebook 2 — Cohort retention:** 27 monthly cohorts tracked across 12 months. Enterprise retains best, SMB churns fastest in the first 3 months.

**Notebook 3 — Variance engine:** budget vs actual by department across 27 months with materiality flagging at ±10%. Engineering consistently overspent.

**Notebook 4 — Scenario analysis:** upside, base, and downside projections 12 months forward. Gap between best and worst case is $12.5M annualized.

## Phase 4 — Power BI Dashboard ✓ (March 2026)
Built an executive dashboard connected to forge.db. Includes 4 KPI cards (Total Revenue, ARR, MRR, Headcount) and 3 charts (revenue by segment, monthly trend, budget vs actual). Saved as powerbi/forge_dashboard.pbix.

## Phase 5 — HTML Portfolio Page (next)
Build portfolio page, deploy via GitHub Pages, update README with live URL.
