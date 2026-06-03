from sqlalchemy import create_engine
import pandas as pd

engine = create_engine("sqlite:///data/db/bluestock_mf.db")

nav_df = pd.read_csv('data/processed/02_nav_history_cleaned.csv')
txn_df = pd.read_csv('data/processed/08_investor_transactions_cleaned.csv')
pref_df = pd.read_csv('data/processed/07_scheme_performance_cleaned.csv')


nav_df.to_sql("fact_nav",engine,if_exists="replace", index = False )
txn_df.to_sql('facr_transaction',engine,if_exists="replace",index = False )
pref_df.to_sql('fact_performance',engine,if_exists="replace",index = False)


print("Database loaded successfully!")

print('nav_df row count:',len(nav_df))
print('txn_df row count:',len(txn_df))
print('pref_df row count:',len(pref_df))


