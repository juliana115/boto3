# Using Client Method
import boto3

s3_client = boto3.client('s3')
copy_source = {
    'Bucket': 'source-bucket-name',
    'Key': 'source-object-key'
}
s3_client.copy(copy_source, 'destination-bucket-name', 'destination-object-key')


# Using Resource  Method

import boto3

s3 = boto3.resource('s3')
copy_source = {
    'Bucket': 'source-bucket-name',
    'Key': 'source-object-key'
}
s3.Bucket('destination-bucket-name').copy(copy_source, 'destination-object-key')
