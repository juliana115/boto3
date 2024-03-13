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

# Usage example
s3_connection = boto3.client('s3')
bucket_prefix = "firsts3bucket"
bucket_name, bucket_response = create_bucket(bucket_prefix, s3_connection)
