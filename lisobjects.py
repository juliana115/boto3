import boto3

s3_client = boto3.client('s3')
objects = s3_client.list_objects_v2(Bucket='your-bucket-name')

for obj in objects['Contents']:
    print(obj['Key'])
