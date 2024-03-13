import boto3

def download_file_from_bucket(bucket_name, file_name, local_file_path, s3_connection):
    # Download the file from the specified bucket
    s3_connection.download_file(bucket_name, file_name, local_file_path)
    print(f"File {file_name} downloaded from {bucket_name} to {local_file_path}")

# Usage example
s3_connection = boto3.client('s3')
bucket_name = "firsts3bucket-unique-id" # Replace with your actual bucket name
file_name = "file.txt"
local_file_path = "downloaded_file.txt"

download_file_from_bucket(bucket_name, file_name, local_file_path, s3_connection)
