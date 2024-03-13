import boto3

def delete_object_from_s3(bucket_name, object_key):
    s3_client = boto3.client('s3')
    response = s3_client.delete_object(Bucket=bucket_name, Key=object_key)
    return response

# Example usage
bucket_name = 'your-bucket-name'
object_key = 'path/to/your/object'
response = delete_object_from_s3(bucket_name, object_key)
print(response)
