import boto3
import uuid

def create_bucket_name(bucket_prefix):
    # Generate a unique bucket name with the given prefix
    return '-'.join([bucket_prefix, str(uuid.uuid4())])

def create_bucket(bucket_prefix, s3_connection):
    session = boto3.session.Session()
    current_region = session.region_name
    bucket_name = create_bucket_name(bucket_prefix)
    
    # Conditionally set CreateBucketConfiguration based on the region
    if current_region == 'us-east-1':
        bucket_response = s3_connection.create_bucket(Bucket=bucket_name)
    else:
        bucket_response = s3_connection.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration={'LocationConstraint': current_region})
    
    print(bucket_name, current_region)
    return bucket_name, bucket_response

def upload_file_to_bucket(bucket_name, file_name, file_content, s3_connection):
    # Upload a file to the specified bucket
    s3_connection.put_object(Bucket=bucket_name, Key=file_name, Body=file_content)
    print(f"File {file_name} uploaded to {bucket_name}")

# Usage example
s3_connection = boto3.client('s3')
bucket_prefix = "firsts3bucket"
bucket_name, bucket_response = create_bucket(bucket_prefix, s3_connection)

# Example of uploading a file to the created bucket
file_name = "file.txt"
file_content = b"Hello, this is a test file into boto."
upload_file_to_bucket(bucket_name, file_name, file_content, s3_connection)
