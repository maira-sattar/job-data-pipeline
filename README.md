An end-to-end data engineering project that pulls UK data analyst job postings from the Adzuna API, cleans them with Python, loads them into Google BigQuery, orchestrates the workflow with Apache Airflow, and reports on them in a Tableau dashboard.

<p align="center">
  <img src="https://skillicons.dev/icons?i=python,docker,git,github" alt="Python, Docker, Git, and GitHub" />
  <img src="https://cdn.simpleicons.org/apacheairflow/017CEE" height="48" alt="Apache Airflow" />
  <img src="https://cdn.simpleicons.org/googlebigquery/669DF6" height="48" alt="Google BigQuery" />
  <img src="https://cdn.simpleicons.org/tableau/E97627" height="48" alt="Tableau" />
  <img src="https://cdn.simpleicons.org/json/000000" height="48" alt="JSON" />
</p>

## Project Overview

This project is an ETL (Extract, Transform, Load) pipeline for job-market data. Raw API responses are kept separate from cleaned data, and the cleaned data is loaded into BigQuery, where a summary table is built for reporting. The steps are modular Python scripts, and an Apache Airflow DAG runs them in order on a daily schedule.

## Tech Stack

| Area | Tools |
|---|---|
| Language | Python (pandas, requests, python-dotenv) |
| Data source | Adzuna Jobs API |
| Orchestration | Apache Airflow 2.9.3 on Docker Compose |
| Cloud | Google Cloud Platform: BigQuery (Sandbox) and IAM service account |
| Reporting | Tableau Public |
| Version control | Git and GitHub |

## Data Pipeline Architecture

<img width="890" height="682" alt="Job market data architecture diagram" src="https://github.com/user-attachments/assets/8104fbaf-55a0-4b92-92b6-0ca7a8a2165f" />

## Pipeline Workflow

1. **Extract:** Call the Adzuna API (UK, search term "data analyst", 50 results per run) and save the raw response as a timestamped JSON file.
2. **Transform:** Use pandas to flatten the nested fields (company, location, category), fill missing contract types, convert dates, add an extraction timestamp, and save the result as a CSV.
3. **Load:** Load the cleaned CSV into the BigQuery table `silver_jobs` using the `google-cloud-bigquery` library. Each run appends new rows.
4. **Orchestrate:** The Airflow DAG `job_market_etl_pipeline` runs extract, then transform, then load, on a daily schedule.
5. **Analyze:** Build the Gold summary table with SQL in BigQuery, export it as a CSV, and visualize it in Tableau Public.

## Data Layers

| Layer | Purpose | Format and location |
|---|---|---|
| Bronze | Raw Adzuna API responses with a timestamp in the file name | JSON files in `data/bronze/` |
| Silver | Cleaned, flattened job records | CSV files in `data/silver/` and the BigQuery table `silver_jobs` |
| Gold | Job count and average salary by location and category | BigQuery table `gold_jobs_by_location_category`, exported to CSV for Tableau |

The Gold table is built with this query (run in the BigQuery console):
```sql
CREATE OR REPLACE TABLE `<your-project>.job_market_data.gold_jobs_by_location_category` AS
SELECT
  location,
  category,
  COUNT(*) AS job_count,
  ROUND(AVG(salary_min), 0) AS avg_salary_min,
  ROUND(AVG(salary_max), 0) AS avg_salary_max
FROM `<your-project>.job_market_data.silver_jobs`
GROUP BY location, category
ORDER BY job_count DESC;
```

## Dashboard

<img width="1505" height="907" alt="Screenshot 2026-10-25 at 11 02 10 PM" src="https://github.com/user-attachments/assets/f7c6bee8-be4d-4be0-9f90-787355f3e616" />

## ⚙️ Getting Started

### Prerequisites
- Git
- Python
- Docker Desktop
- A free [Adzuna API](https://developer.adzuna.com) app ID and key
- A Google Cloud project with BigQuery (the free Sandbox works, no billing needed)
- A service account JSON key with the **BigQuery Data Editor** and **BigQuery Job User** roles


### 1. Clone the Repository

```bash
git clone https://github.com/maira-sattar/job-data-pipelines.git
```

### 2. Navigate to the Project Directory

```bash
cd job-data-pipelines
```

### 3. Add Your Credentials

Save your service account key as `credentials.json` in the project root. Then create a `.env` file in the project root:

```
ADZUNA_APP_ID=your_adzuna_app_id
ADZUNA_APP_KEY=your_adzuna_app_key
GOOGLE_APPLICATION_CREDENTIALS=credentials.json
BQ_PROJECT_ID=your-gcp-project-id
AIRFLOW_UID=50000
```

Both files are listed in `.gitignore` and must never be committed. Docker Compose mounts `src/`, `.env` and `credentials.json` into the Airflow containers.

### 4. Start the Docker Environment

Make sure Docker Desktop is running. Initialize Airflow once, then start it:

```bash
docker compose up airflow-init
```

```bash
docker compose up -d
```

### 5. Access Apache Airflow

Open `http://localhost:8080` and sign in with the default local credentials from the official Airflow Compose file (username `airflow`, password `airflow`).

### 6. Run the Pipeline

Find the `job_market_etl_pipeline` DAG, turn it on, and trigger a run. When extract, transform and load all turn green, check that the `silver_jobs` table in your BigQuery dataset has new rows.




