import boto3

s3 = boto3.resource('s3')
my_bucket = s3.Bucket('your-bucket-name')

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object.key)
