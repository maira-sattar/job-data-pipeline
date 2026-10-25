# Job Data Pipelines

A data engineering project focused on extracting, transforming, and organizing job-market data into structured datasets for analytics and dashboard reporting.

## 🛠️ Technologies Used

<p align="left">
  <img src="https://skillicons.dev/icons?i=python,docker,git,github" alt="Python, Docker, Git, and GitHub" />
</p>

- **Python** — Data extraction and transformation
- **Apache Airflow** — Workflow orchestration
- **Docker Compose** — Local environment setup
- **JSON and CSV** — Data storage formats
- **Git and GitHub** — Version control and project management

## 📌 Project Overview

This project demonstrates an ETL (Extract, Transform, Load) pipeline for processing job-market data. It separates raw data from cleaned data and prepares structured outputs for analysis.

The pipeline is organized into modular Python scripts and an Apache Airflow DAG to support workflow orchestration and data processing.

## 🏗️ Data Pipeline Architecture

```text
Job-Market Data
       |
       v
   Extraction
   (Python)
       |
       v
 Bronze Layer
   (Raw JSON)
       |
       v
 Transformation
   (Python)
       |
       v
 Silver Layer
 (Cleaned CSV)
       |
       v
 Gold / Analytics
 (Summary Dataset)
       |
       v
 Dashboard & Insights
```

## 🔄 Pipeline Workflow

1. **Extract:** Collect job-market data and save raw records in JSON format.
2. **Transform:** Clean and process the extracted data using Python.
3. **Load:** Store processed records in CSV format for downstream analysis.
4. **Orchestrate:** Use Apache Airflow to define and manage pipeline tasks.
5. **Analyze:** Prepare summarized job-market data for dashboard reporting.

## 📂 Project Structure

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

*Note: Update the folder and file names above if your actual repository structure differs. Rename `dashbaords` to `dashboards` in your project if you haven't already.*

## 🥉 Data Layers

| Layer | Purpose | Format |
|---|---|---|
| Bronze | Stores extracted raw job-market records | JSON |
| Silver | Stores cleaned and transformed records | CSV |
| Gold / Analytics | Stores summarized data for reporting | CSV |

## 📊 Dashboard

The dashboard provides a visual way to explore the processed job-market data.

To display your dashboard screenshot on GitHub:

1. Create a `dashboards` folder if it doesn't exist.
2. Add your screenshot to that folder.
3. Name it `dashboard-screenshot.png`.

![Job Market Dashboard](dashboards/dashboard-screenshot.png)

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

*Follow the configuration and execution steps defined in your actual Docker Compose file and DAG.*

## 🎯 Key Learning Outcomes

- Designing modular ETL pipelines with Python
- Separating raw and cleaned data into Bronze and Silver layers
- Organizing and orchestrating workflows using Apache Airflow
- Managing a local data engineering environment with Docker Compose
- Preparing structured datasets for dashboard reporting
- Using Git and GitHub to manage project versions

## 🚀 Future Improvements

- Add automated data-quality validation
- Implement a dedicated Gold data layer
- Improve pipeline logging and error handling
- Integrate a database or cloud data warehouse
- Automate dashboard data refreshes

## 👩‍💻 Author

**Maira Sattar**

- GitHub: [@maira-sattar](https://github.com/maira-sattar)

---

*Built as a practical data engineering project to demonstrate ETL workflow development and data pipeline orchestration.*
