import glob
import os
from google.cloud import bigquery
from dotenv import load_dotenv
import pandas as pd

# Load environment variables from .env
load_dotenv('/opt/airflow/.env')
project_id = os.getenv("BQ_PROJECT_ID")
credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "credentials.json")

if not os.path.exists(credentials_path):
    credentials_path = "/opt/airflow/credentials.json"

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = credentials_path

client = bigquery.Client(project=project_id)
silver_files = sorted(glob.glob("data/silver/jobs_clean_*.csv"))
latest_file = silver_files[-1]

print(f"Loading: {latest_file}")
df = pd.read_csv(latest_file)
print(f"Rows to load: {len(df)}")

dataset_id = "job_market_data"
dataset_ref = bigquery.DatasetReference(project_id, dataset_id)

try:
    client.get_dataset(dataset_ref)
    print(f"Dataset {dataset_id} already exists")
except Exception:
    dataset = bigquery.Dataset(dataset_ref)
    dataset.location = "US"
    client.create_dataset(dataset)
    print(f"Created dataset {dataset_id}")

# Load table logic (placed outside try/except so it runs regardless of whether dataset existed or was just created)
table_id = f"{project_id}.{dataset_id}.silver_jobs"
job_config = bigquery.LoadJobConfig(
    write_disposition="WRITE_APPEND"  # adds new rows each run, doesn't overwrite
)

job = client.load_table_from_dataframe(df, table_id, job_config=job_config)
job.result()  # wait for it to finish

print(f"Loaded {len(df)} rows into {table_id}")