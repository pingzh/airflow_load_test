
Some settings:

1. Set `default_pool` to -1 so that airflow tasks aren’t throttled by pool number

2. Env vars:

```
# the following two vars ensure no limit when enqueuing tasks
export AIRFLOW__CORE__EXECUTOR=CeleryExecutor
export AIRFLOW__CORE__PARALLELISM=0
export AIRFLOW__SCHEDULER__MAX_TIS_PER_QUERY=0
```
