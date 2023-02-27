from airflow.utils.dates import days_ago
from airflow import DAG
from airflow.operators.dummy_operator import DummyOperator
from airflow.operators.python_operator import PythonOperator
from dags.plugins.function import main

DEFAULT_ARGS = {
    'start_date': days_ago(1),
    'owner': 'фglukhov',
    'poke_interval': 600,
    'catchup': False,
    'depends_on_past': False
}

with DAG(
        'test_script_for_aero',
        schedule_interval='0 */12 * * *',
        default_args=DEFAULT_ARGS,
        tags=['test'],
        ) as dag:

    task1 = DummyOperator(task_id='start',
                          dag = dag
                         )

    task2 = PythonOperator(task_id='my_main_task',
                python_callable=main,
                dag=dag
                )

    task3 = DummyOperator(task_id='end',
                          dag=dag
                          )

    task1 >> task2 >> task3
