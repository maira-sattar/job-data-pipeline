import json;
import glob;
import pandas as pd;
import datetime;
import os;
bronze_file=sorted(glob.glob("data/bronze/jobs_raw_*.json"))
latest_file=bronze_file[-1]
print(f"Reading: {latest_file}")
with open(latest_file,"r") as f:
    raw_data=json.load(f)
    jobs = raw_data.get("results",[])
    rows=[]
    for jobs in jobs:
        rows.append({
            "id":jobs.get("id"),
            "title":jobs.get("title"),
            "company":jobs.get("company",{}).get("display_name"),
            "location":jobs.get("location",{}).get("display_name"),
            "contract_type":jobs.get("contract_type"),
            "category":jobs.get("category",{}).get("label"),
            "salary_min":jobs.get("salary_min"),
            "salary_max":jobs.get("salary_max"),
            "created":jobs.get("created"),
            "description":jobs.get("description"),
        })
        df=pd.DataFrame(rows)
        print("Columns:", list(df.columns))
        print("Shape:", df.shape) 
        print("\nNulls per column:")
        df['contract_type'] = df['contract_type'].fillna('not_specified')
        df['created'] = pd.to_datetime(df['created']) 
        df['description_short'] = df['description'].str[:150]
        df['extracted_at'] = datetime.datetime.now()
        os.makedirs('data/silver', exist_ok=True) 
        timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
        silver_path = f"data/silver/jobs_clean_{timestamp}.csv" 
        df.to_csv(silver_path, index=False) 
        print(f"Saved clean data to {silver_path}")
        print(df.isnull().sum())
        print("\nDuplicate rows:", df.duplicated().sum())
        print("Duplicate IDs:", df['id'].duplicated().sum())