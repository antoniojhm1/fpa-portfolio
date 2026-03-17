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
- 7,853 revenue transactions (Jan 2024 – Mar 2026)
- 42 employees across 5 departments
- 135 months of budget vs actual data

## Phase 2 — SQL Database ✓ COMPLETE (March 17 2026)
- [x] Created SQLite database (forge.db) from 5 CSV files
- [x] Written SQL query library (queries.sql) with 7 core queries
- [x] Revenue by segment — Enterprise $14M, Mid-Market $8.4M, SMB $2.3M
- [x] Total ARR — $18.8M across 500 customers
- [x] Budget vs actual — all departments over budget, G&A worst at +5.5%
- [x] JOIN queries connecting customers, contracts, revenue tables

## Phase 3 — Python Modeling (IN PROGRESS)
- [x] Jupyter notebook setup complete
- [x] Notebook 1: Revenue forecast complete
  - Historical trend analysis Jan 2024 – Mar 2026
  - 6-month forward forecast (Apr–Sep 2026)
  - Trend slope: -$3,797/month (plateau phase)
  - Charts saved: revenue_trend.png, revenue_forecast.png
- [ ] Notebook 2: Cohort retention analysis
- [ ] Notebook 3: Variance engine

## Phase 4 — Power BI Dashboard (UPCOMING)
- [ ] Connect Power BI to SQLite
- [ ] Build executive dashboard

## Phase 5 — Portfolio HTML Page (UPCOMING)
- [ ] Build public portfolio page
- [ ] Deploy via GitHub Pages