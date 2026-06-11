# Bluestock Fintech — Mutual Fund Analytics Platform
### Capstone Project 

---

## Project Overview
A full-stack Mutual Fund Analytics Platform built using real Indian
mutual fund data from AMFI India and mfapi.in. The project covers
a complete data pipeline — from raw data ingestion to interactive
Power BI dashboard — analyzing NAV trends, fund performance, investor
demographics, and SIP market trends across 10 major AMCs.

---

## Tech Stack
- Python 3.10+
- Pandas, NumPy, Matplotlib, Seaborn
- SQLite + SQLAlchemy
- Power BI Desktop
- Git + GitHub
- Jupyter Lab

---
## Project Structure


bluestock_mf_capstone/
├── data/
│   ├── raw/           
│   ├── processed/     
│   └── db/            
├── notebooks/
│   ├── 01_data_ingestion.ipynb
│   ├── 02_data_cleaning.ipynb
│   ├── 03_eda_analysis.ipynb
│   ├── 04_performance_analytics.ipynb
│   └── 05_advanced_analytics.ipynb
├── scripts/
│   ├── etl_pipeline.py
│   ├── live_nav_fetch.py
│   ├── run_pipeline.py 
│   └── recommender.py
├── sql/
│   ├── schema.sql
│   └── queries.sql
├── dashboard/
│   └── bluestock_mf.pbix
├── reports/
│   ├── Final_Report.pdf
│   └── Presentation.pptx
└── README.md
---

## Dataset Description

| File | Rows | Description |
|---|---|---|
| clean_fund_master.csv | 40 | Scheme metadata |
| clean_nav_history.csv | 46,000+ | Daily NAV 2022–2025 |
| clean_aum_fund_house.csv | 90 | Quarterly AUM by AMC |
| clean_sip_inflows.csv | 48 | Monthly SIP industry data |
| clean_category_inflows.csv | 144 | Net inflows by category |
| clean_folio_growth.csv | 21 | Total folios growth |
| clean_scheme_performance.csv | 40 | Risk and return metrics |
| clean_investor_transactions.csv | 32,000+ | Investor transactions |
| clean_portfolio_holdings.csv | 320 | Fund stock holdings |
| clean_benchmark_indices.csv | 8,050 | Daily benchmark data |

---

## How to Run

### 1. Clone the repository

git clone https://github.com/Manideep685/bluestock-mf-capstone
cd bluestock-mf-capstone

### 2. Install dependencies

pip install pandas numpy matplotlib seaborn sqlalchemy jupyter

### 3. Run master pipeline

python run_pipeline.py

### 4. jupyter lab

Open notebooks in this order:
1. etl_pipeline.ipynb
2. eda_analysis.ipynb
3. performance_metrics.ipynb
4. Advanced_Analytics.ipynb

### 5. Open Power BI dashboard
- Open Power BI Desktop
- File → Open → dashboard/bluestock_mf_dashboard.pbix

### 6. Run fund recommender

Enter risk appetite when prompted: Low / Moderate / High

---

## Key Findings
- SIP inflows reached ₹31,002 Cr milestone in Dec 2025
- Total folios grew from 13.26 Cr (Jan 2022) to 26.12 Cr (Dec 2025)
- SBI Mutual Fund leads industry AUM among top 10 AMCs
- Mid cap and small cap funds show highest 3yr returns
- Tier 1 cities account for majority of investor transactions
- 2022 investor cohort shows highest avg investment per person

---

## Deliverables

| Deliverable | Location |
|---|---|
| ETL Pipeline | notebooks/etl_pipeline.ipynb |
| Star Schema | schema.sql |
| EDA Notebook | notebooks/eda_analysis.ipynb |
| Performance Metrics | notebooks/performance_metrics.ipynb |
| Power BI Dashboard | dashboard/bluestock_mf_dashboard.pbix |
| Advanced Analytics | notebooks/Advanced_Analytics.ipynb |
| Final Report | docs/Final_Report.pdf |
| Presentation | docs/Bluestock_MF_Presentation.pptx |

---

## Author
**G. Manideep**
Data Analyst Intern — Bluestock Fintech Pvt. Ltd.
GitHub: github.com/Manideep685
LinkedIn: linkedin.com/in/g-manideep-3b4832257
