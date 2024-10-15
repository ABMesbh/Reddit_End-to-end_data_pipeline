from utils.constants import Aws_access_key_id, Aws_secret_key
import s3fs

def connect_to_s3():
    try :
        s3 = s3fs.S3FileSystem(anon=False,
                               key=Aws_access_key_id,
                               secret=Aws_secret_key)
        print('Connected to s3')
        return s3
    except Exception as e:
        print(e)

def create_bucket_if_not_exist(s3 : s3fs.S3FileSystem , bucket : str):
    try:
        if not s3.exists(bucket):
            s3.mkdir(bucket)
            print('Bucket created')
        else : 
            print('Bucket already exists')
    except Exception as e:
        print(e)


def upload_to_s3(s3 : s3fs.S3FileSystem , file_path: str,  bucket : str, s3_file_name: str):
    try:
        s3.put(file_path, bucket + '/raw/' + s3_file_name )
        print('File uploaded to S3')
    except FileNotFoundError:
        print('The file was not found')