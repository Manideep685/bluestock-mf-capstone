import pandas as pd

nav_df = pd.read_csv('data/raw/02_nav_history.csv')

nav_df["date"] = pd.to_datetime(nav_df["date"])

nav_df = nav_df.sort_values(["amfi_code","date"])

nav_df["nav"] = nav_df.groupby("amfi_code")["nav"].ffill()

nav_df = nav_df.drop_duplicates()

nav_df = nav_df[nav_df['nav']>0]

nav_df.to_csv('data/processed/02_nav_history_cleaned.csv', index = False)

print("NAV History cleaned successfully!")

print("shape:",nav_df.shape)

txn_df = pd.read_csv("data/raw/08_investor_transactions.csv")

txn_df["transaction_date"] = pd.to_datetime(txn_df["transaction_date"])

txn_df["transaction_type"] = txn_df["transaction_type"].str.strip().str.title()

valid_type = ["Sip", "Lumpsum", "Redemption"]
txn_df = txn_df[txn_df["transaction_type"].isin(valid_type)]

txn_df = txn_df[txn_df['amount_inr']>0]

txn_df['kyc_status'] = txn_df['kyc_status'].str.strip().str.upper()

txn_df = txn_df.drop_duplicates()

txn_df.to_csv('data/processed/08_investor_transactions_cleaned.csv', index = False)

print('Investors transaction was cleaned successfully!')

print('shape:', txn_df.shape)

pref_df = pd.read_csv('data/raw/07_scheme_performance.csv')

return_cols = [
    "return_1yr_pct",
    "return_3yr_pct",
    "return_5yr_pct",
    "benchmark_3yr_pct",
    "alpha",
    "beta",
    "sharpe_ratio",
    "sortino_ratio",
    "std_dev_ann_pct",
    "max_drawdown_pct",
    "aum_crore",
    "expense_ratio_pct"
]

for col in return_cols:
    pref_df[col] = pd.to_numeric(pref_df[col], errors="coerce")

pref_df = pref_df.dropna(subset = ['expense_ratio_pct'])

pref_df = pref_df[
    (pref_df['expense_ratio_pct'] >= 0.1 )&
    (pref_df['expense_ratio_pct'] <= 2.5 )
]

pref_df = pref_df.drop_duplicates()

pref_df.to_csv('data/processed/07_scheme_performance_cleaned.csv', index = False)

print("Scheme performance cleaned successfully!")
print("shape:", pref_df.shape)





