import boto3

def delete_bucket(bucket_name):
    s3 = boto3.resource('s3')
    bucket = s3.Bucket(bucket_name)
    
    # Delete all objects in the bucket
    bucket.objects.all().delete()
    
    # Delete the bucket
    bucket.delete()

# Example usage
bucket_name = 'your-bucket-name'
delete_bucket(bucket_name)
