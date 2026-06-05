from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///data/db/bluestock_mf.db")

nav_df = pd.read_csv('data/processed/clean_nav_history.csv')
txn_df = pd.read_csv('data/processed/clean_investor_transactions.csv')
pref_df = pd.read_csv('data/processed/clean_scheme_performance.csv')
fund_df = pd.read_csv('data/processed/clean_fund_master.csv')
aum_df = pd.read_csv('data/processed/clean_aum_fund_house.csv')
sip_df = pd.read_csv('data/processed/clean_sip_inflows.csv')
folio_df = pd.read_csv('data/processed/clean_folio_growth.csv')
cat_df = pd.read_csv('data/processed/clean_category_inflows.csv')
holdings_df = pd.read_csv('data/processed/clean_portfolio_holdings.csv')
benchmark_df = pd.read_csv('data/processed/clean_benchmark_indices.csv')



nav_df.to_sql("fact_nav",engine,if_exists="replace", index = False )
txn_df.to_sql('facr_transaction',engine,if_exists="replace",index = False )
pref_df.to_sql('fact_performance',engine,if_exists="replace",index = False)
fund_df.to_sql("fund_master", engine, if_exists="replace", index=False)
aum_df.to_sql("fact_aum", engine, if_exists="replace", index=False)
sip_df.to_sql("sip_inflows", engine, if_exists="replace", index=False)
folio_df.to_sql("folio_growth", engine, if_exists="replace", index=False)
cat_df.to_sql("category_inflows", engine, if_exists="replace", index=False)
holdings_df.to_sql("portfolio_holdings", engine, if_exists="replace", index=False)
benchmark_df.to_sql("benchmark_returns", engine, if_exists="replace", index=False)

print("Database loaded successfully!")

print('nav_df row count:',len(nav_df))
print('txn_df row count:',len(txn_df))
print('pref_df row count:',len(pref_df))
print('fund_df row count:',len(fund_df))
print('aum_df row count:',len(aum_df))
print('sip_df row count:',len(sip_df))
print('folio_df row count:',len(folio_df))
print('cat_df row count:',len(cat_df))
print('holdings_df row count:',len(holdings_df))
print('bench_df row count:',len(benchmark_df))


