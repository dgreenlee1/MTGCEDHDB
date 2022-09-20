import json
import boto3
from bs4 import BeautifulSoup


s3_client = boto3.client("s3")
S3_BUCKET = 'pythontestbucket2022'


def lambda_handler(event, context):
    
    session = boto3.Session()
    bucket_arn = "s3://pythontestbucket2022"
    s3 = session.resource("s3")
    bucket = s3.Bucket("pythontestbucket2022")
    index = 0
    

    for my_bucket_object in bucket.objects.all():
        print(my_bucket_object.key)
        file_content = s3_client.get_object(
            Bucket=S3_BUCKET, Key=my_bucket_object.key)["Body"].read()
        print(file_content[0:20])
        soup = BeautifulSoup(file_content, "html.parser") # Make soup
        index += 1
        if index == 1:          # It takes a really long time to make the soup, one at a time only
            break
    

    return {
        'statusCode': 200,
        'body': json.dumps('Hello from Lambda!')
    }
