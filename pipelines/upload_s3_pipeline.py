from etls.aws_etl import connect_to_s3, create_bucket_if_not_exist, upload_to_s3
from utils.constants import Aws_bucket_name


def upload_s3_pipeline(ti):
    file_path = ti.xcom_pull(task_ids = 'Reddit_extraction', key = 'return_value')

    s3 = connect_to_s3()

    create_bucket_if_not_exist(s3, Aws_bucket_name)
    upload_to_s3(s3, file_path, Aws_bucket_name, file_path.split('/')[-1])