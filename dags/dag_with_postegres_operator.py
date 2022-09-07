import airflow
from datetime import timedelta
from airflow import DAG
from airflow.operators.postgres_operator import PostgresOperator
from airflow.utils.dates import days_ago
from airflow.operators.python import PythonOperator
from scripts import main

args = {'owner': 'airflow'}

default_args = {
    'owner': 'airflow',
    'start_date': airflow.utils.dates.days_ago(2),
    'depends_on_past': True,
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 2,
    'retry_delay': timedelta(minutes=5),
}

dag = DAG(
    dag_id="pizzeria_info_v4",
    default_args=default_args,
    schedule_interval='0 0 * * *',
    start_date=airflow.utils.dates.days_ago(1)
)

data_generating = PythonOperator(
    dag=dag,
    task_id="customers_orders_data_generator",
    python_callable=main.generate_data,

)

data_generating
