# run_pipeline.py
# Master execution script — Bluestock MF Capstone

import sys
import os
import pandas as pd

def check_dependencies():
    """Check all required libraries are installed."""
    required = [
        'pandas', 'numpy', 'matplotlib',
        'seaborn', 'sqlalchemy', 'scipy'
    ]
    missing = []
    for lib in required:
        try:
            __import__(lib)
        except ImportError:
            missing.append(lib)
    if missing:
        print(f"Missing libraries: {missing}")
        print("Run: pip install " + " ".join(missing))
        sys.exit(1)
    print("All dependencies found")

def check_data_files():
    """Check all required CSV files exist."""
    required_files = [
        'data/processed/clean_fund_master.csv',
        'data/processed/clean_nav_history.csv',
        'data/processed/clean_aum_fund_house.csv',
        'data/processed/clean_sip_inflows.csv',
        'data/processed/clean_category_inflows.csv',
        'data/processed/clean_folio_growth.csv',
        'data/processed/clean_scheme_performance.csv',
        'data/processed/clean_investor_transactions.csv',
        'data/processed/clean_portfolio_holdings.csv',
        'data/processed/clean_benchmark_indices.csv'
    ]
    missing = []
    for f in required_files:
        if not os.path.exists(f):
            missing.append(f)
    if missing:
        print("Missing data files:")
        for f in missing:
            print(f"  {f}")
        sys.exit(1)
    print("All data files found")

def check_outputs():
    """Check all expected output files exist."""
    outputs = [
        'var_cvar_report.csv',
        'data/processed/alpha_beta.csv',
        'charts/rolling_sharpe_chart.png',
        'dashboard/bluestock_mf_dashboard.pbix'
    ]
    print("\nOutput files status:")
    for f in outputs:
        status = "✓ Found" if os.path.exists(f) else "✗ Missing"
        print(f"  {status} — {f}")

def run_recommender():
    """Run fund recommender for all risk levels."""
    sys.path.insert(0, '.')
    try:
        from recommender import recommend_funds
        recommend_funds('Low')
        recommend_funds('Moderate')
        recommend_funds('High')
    except Exception as e:
        print(f"Recommender error: {e}")

def main():
    # Change to capstone root directory
    script_dir = os.path.dirname(os.path.abspath(__file__))
    root_dir = os.path.dirname(script_dir)
    os.chdir(root_dir)
    print(f"Working directory: {os.getcwd()}")

    print("=" * 50)
    print("Bluestock MF Capstone — Master Pipeline")
    print("=" * 50)

    # Step 1 - Check dependencies
    print("\nStep 1 — Checking dependencies")
    check_dependencies()

    # Step 2 - Check data files
    print("\nStep 2 — Checking data files")
    check_data_files()

    # Step 3 - Check outputs
    print("\nStep 3 — Checking output files")
    check_outputs()

    # Step 4 - Run recommender
    print("\nStep 4 — Fund recommender test")
    run_recommender()

    # Step 5 - Final summary
    print("\n" + "=" * 50)
    print("Pipeline Verification Complete")
    print("=" * 50)
    print("\nTo run full analysis open Jupyter Lab:")
    print("  jupyter lab")
    print("\nNotebooks to run in order:")
    print("  1. notebooks/etl_pipeline.ipynb")
    print("  2. notebooks/eda_analysis.ipynb")
    print("  3. notebooks/performance_metrics.ipynb")
    print("  4. notebooks/Advanced_Analytics.ipynb")
    print("\nDashboard:")
    print("  Open dashboard/bluestock_mf_dashboard.pbix in Power BI")

if __name__ == "__main__":
    main()