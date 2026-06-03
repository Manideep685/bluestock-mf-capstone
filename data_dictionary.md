# Data Dictionary

# nav_history.csv

| Column    | Type    | Description              |
| --------- | ------- | ------------------------ |
| amfi_code | Integer | Unique AMFI scheme code  |
| date      | Date    | NAV valuation date       |
| nav       | Float   | Net Asset Value per unit |


# investor_transactions.csv

| Column           | Type    | Description                |
| ---------------- | ------- | -------------------------- |
| investor_id      | Integer | Unique investor identifier |
| amfi_code        | Integer | Mutual fund scheme code    |
| transaction_date | Date    | Transaction date           |
| transaction_type | Text    | SIP/Lumpsum/Redemption     |
| amount           | Float   | Transaction amount         |
| investor_state   | Text    | State of investor          |
| kyc_status       | Text    | KYC verification status    |

# scheme_performance.csv

| Column         | Type    | Description                      |
| -------------- | ------- | -------------------------------- |
| amfi_code      | Integer | Mutual fund code                 |
| scheme_name    | Text    | Fund name                        |
| category       | Text    | Fund category                    |
| return_1yr_pct | Float   | 1-year return                    |
| return_3yr_pct | Float   | 3-year return                    |
| return_5yr_pct | Float   | 5-year return                    |
| alpha          | Float   | Alpha measure                    |
| beta           | Float   | Beta measure                     |
| sharpe         | Float   | Sharpe ratio                     |
| expense_ratio  | Float   | Expense ratio (%)                |
| aum_cr         | Float   | Assets Under Management (Crores) |
