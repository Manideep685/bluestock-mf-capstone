import pandas as pd 
import os 

raw_path = "data/raw"

csv_files = [f for f in os.listdir(raw_path)if f.endswith(".csv")]

for file in csv_files:
    file_path = os.path.join (raw_path,file)

    df = pd.read_csv(file_path)

    print("\n"+ "="*50)
    print(f"File : {file}")
    print(f"shape :{df.shape}")
    print("\n Data type")
    print(df.dtypes)
    print("\nFirst 5 rows")
    print(df.head())

print("\n Data Ingestion completed successfully!")
