from airflow import DAG
from airflow.operators.python import PythonOperator
import os
from datetime import datetime
import sys

sys.path.insert(0 , os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from pipelines.upload_s3_pipeline import upload_s3_pipeline
from pipelines.reddit_pipeline import reddit_pipeline


default_args = {
    'owner' : 'M.A',
    'start_date': datetime(2023, 10, 22)
}

file_postfix = datetime.now().strftime("%Y%m%d")

dag = DAG(
    dag_id='etl_reddit_pipeline',
    default_args= default_args,
    schedule_interval = '@daily',
    catchup=False,
    tags=['reddit', 'etl', 'pipeline'],
)

# extraction from reddit

extract = PythonOperator(
    task_id = 'Reddit_extraction',
    python_callable = reddit_pipeline,
    op_kwargs =  {
        'file_name' : f'reddit_{file_postfix}',
        'subreddit' : 'dataengineering',
        'time_filter': 'day',
        'limit': 100
    },
    dag = dag


)

# Upload to our S3 Bucket

upload_s3 = PythonOperator(
    task_id = 's3_upload',
    python_callable = upload_s3_pipeline,
    dag = dag

)

extract >> upload_s3