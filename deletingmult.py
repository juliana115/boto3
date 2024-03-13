import boto3
from boto3.session import Session

session = Session(aws_access_key_id='your_key_id',
                 aws_secret_access_key='your_secret_key')

s3_resource = session.resource('s3')
my_bucket = s3_resource.Bucket("your_bucket_name")

response = my_bucket.delete_objects(
    Delete={
        'Objects': [
            {
                'Key': "your_file_name_key"   # the_name of_your_file
            }
        ]
    }
)
