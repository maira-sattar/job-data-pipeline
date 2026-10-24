from datetime import datetime
from airflow import DAG
from airflow.operators.bash import BashOperator

with DAG(
    dag_id="job_market_etl_pipeline",
    start_date=datetime(2026, 8, 1),
    schedule_interval="@daily",
    catchup=False,
    tags=["portfolio", "etl"],
) as dag:

    extract = BashOperator(
        task_id="extract",
        bash_command="cd /opt/airflow/src && python extract.py",
    )

    transform = BashOperator(
        task_id="transform",
        bash_command="cd /opt/airflow/src && python transform.py",
    )

    load = BashOperator(
        task_id="load",
        bash_command="cd /opt/airflow/src && python load.py",
    )

    extract >> transform >> load