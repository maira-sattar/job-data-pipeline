# Job Data Pipelines

A data engineering project focused on extracting, transforming, and organizing job-market data into structured datasets for analytics and dashboard reporting.


<p align="center">
  <img src="https://skillicons.dev/icons?i=python,docker,git,github" alt="Python, Docker, Git, and GitHub" />
</p>



## Project Overview

This project demonstrates an ETL (Extract, Transform, Load) pipeline for processing job-market data. It separates raw data from cleaned data and prepares structured outputs for analysis.

The pipeline is organized into modular Python scripts and an Apache Airflow DAG to support workflow orchestration and data processing.

## Data Pipeline Architecture

<img width="890" height="682" alt="Job market data architecture diagram" src="https://github.com/user-attachments/assets/8104fbaf-55a0-4b92-92b6-0ca7a8a2165f" />

## Pipeline Workflow

1. **Extract:** Collect job-market data and save raw records in JSON format.
2. **Transform:** Clean and process the extracted data using Python.
3. **Load:** Store processed records in CSV format for downstream analysis.
4. **Orchestrate:** Use Apache Airflow to define and manage pipeline tasks.
5. **Analyze:** Prepare summarized job-market data for dashboard reporting.

## Project Structure

```text
job-data-pipelines/
├── dags/
│   └── retail_job_pipeline_dag.py
├── data/
│   ├── bronze/
│   └── silver/
├── dashboards/
│   └── gold_jobs_summary.csv
├── src/
│   ├── extract.py
│   ├── transform.py
│   └── load.py
├── docker-compose.yaml
├── .gitignore
└── README.md
```

## Data Layers

| Layer | Purpose | Format |
|---|---|---|
| Bronze | Stores extracted raw job-market records | JSON |
| Silver | Stores cleaned and transformed records | CSV |
| Gold / Analytics | Stores summarized data for reporting | CSV |

## <img width="1505" height="907" alt="Screenshot 2026-10-25 at 11 02 10 PM" src="https://github.com/user-attachments/assets/f7c6bee8-be4d-4be0-9f90-787355f3e616" />
Dashboard



## ⚙️ Getting Started

### Prerequisites

- Git
- Python
- Docker Desktop

### 1. Clone the Repository

```bash
git clone https://github.com/maira-sattar/job-data-pipelines.git
```

### 2. Navigate to the Project Directory

```bash
cd job-data-pipelines
```

### 3. Start the Docker Environment

Ensure Docker Desktop is running, then execute:

```bash
docker compose up -d
```

### 4. Access Apache Airflow

Open the Airflow web interface using the host port configured in your `docker-compose.yaml` file.

Use the credentials configured in your Airflow environment.

### 5. Run the Pipeline

Locate the `retail_job_pipeline_dag` DAG in the Airflow interface, enable it if necessary, and trigger a run. Monitor task execution and review the generated output files.



