import requests
import pandas as pd 
import os

def fetch_nav(scheme_code, name):
    url = f"https://api.mfapi.in/mf/{scheme_code}"
    response = requests.get(url)
    data = response.json()
    df = pd.DataFrame(data['data'])
    df.to_csv(f"data/raw/{name}.csv", index=False)
    print(f"{name} saved! shape: {df.shape}")
    return df
fetch_nav(125497,"HDFC_TOP100")
fetch_nav(119551,"SBI_BLueschip")
fetch_nav(120503,"ICICI_Bluechip")
fetch_nav(118632,"Nippon_LargeCap")
fetch_nav(119092,"Axis_Bluechip")
fetch_nav(120841,"kotak_Bluechip")

print("All NAV data fetched successfully!")