import requests
import pandas as pd

print("Downloading NYC 311 data via Socrata Open Data API...")

url = "https://data.cityofnewyork.us/resource/erm2-nwe9.csv"
params = {
    "$limit": 500000,
    "$order": "created_date DESC",
    "$select": "unique_key,created_date,closed_date,agency,complaint_type,descriptor,borough,latitude,longitude,status"
}

response = requests.get(url, params=params, timeout=120)

with open("data_raw.csv", "wb") as f:
    f.write(response.content)

df = pd.read_csv("data_raw.csv")
print(f"Downloaded {len(df):,} records")
print(f"Columns: {list(df.columns)}")
print(f"\nDate range: {df['created_date'].min()} to {df['created_date'].max()}")
print(f"\nBorough distribution:\n{df['borough'].value_counts()}")
print(f"\nTop 10 complaint types:\n{df['complaint_type'].value_counts().head(10)}")
