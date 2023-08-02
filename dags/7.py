from datetime import datetime, timedelta

from airflow import DAG
from airflow.operators.bash import BashOperator
from airflow.operators.dummy import DummyOperator


with DAG(
    dag_id='7',
    schedule_interval='@daily',
    start_date=datetime(2022, 1, 1),
    catchup=True,
    dagrun_timeout=timedelta(minutes=60),
    tags=['example', 'example2'],
    max_active_runs=1,
    max_active_tasks=2000,
) as dag:
    run_this_last = DummyOperator(
        task_id='run_this_last',
    )

    # [START howto_operator_bash]
    run_this = BashOperator(
        task_id='run_after_loop',
        bash_command='echo "hi"',
    )
    # [END howto_operator_bash]

    run_this >> run_this_last

    for i in range(1000):
        task = BashOperator(
            task_id='runme_' + str(i),
            bash_command='echo "{{ task_instance_key_str }}"',
        )
        task >> run_this

    # [START howto_operator_bash_template]
    also_run_this = BashOperator(
        task_id='also_run_this',
        bash_command='sleep 1',
    )
    # [END howto_operator_bash_template]
    also_run_this >> run_this_last

# [START howto_operator_bash_skip]
this_will_skip = BashOperator(
    task_id='this_will_skip',
    bash_command='echo "1xxxxxxxxxxxxxxxxxxx"',
    dag=dag,
)
# [END howto_operator_bash_skip]
this_will_skip >> run_this_last

if __name__ == "__main__":
    dag.cli()
