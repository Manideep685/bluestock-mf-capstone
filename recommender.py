import pandas as pd

performance = pd.read_csv("data/processed/clean_scheme_performance.csv")
fund_master = pd.read_csv("data/processed/clean_fund_master.csv")

def recommend_funds(risk_appetite):
    risk_map = {
        "Low": ["Low", "Low to Moderate"],
        "Moderate": ["Moderate", "Moderately High"],
        "High": ["High", "Very High", "Moderately High"]
    }
    if risk_appetite not in risk_map:
        print("Invalid. Choose: Low, Moderate, or High")
        return
    filtered = performance[
        performance["risk_grade"].isin(risk_map[risk_appetite])
    ].merge(
        fund_master[["amfi_code", "scheme_name", "fund_house", "category"]],
        on="amfi_code", how="left"
    )
    top3 = filtered.nlargest(3, "sharpe_ratio")[
        ["scheme_name", "fund_house", "category", "sharpe_ratio", "risk_grade"]
    ].reset_index(drop=True)
    top3.index = top3.index + 1
    print(f"\n=== Top 3 for {risk_appetite} Risk ===")
    print(top3.to_string())
    return top3

if __name__ == "__main__":
    user_input = input("Enter risk appetite (Low / Moderate / High): ")
    recommend_funds(user_input)
