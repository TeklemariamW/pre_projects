import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

# Create an S3 client
s3 = boto3.client('s3')

# Define the bucket name and file details
bucket_name = 'banktekle'
file_path = 'C:/Users/Weldehawariat/Documents/Training/Projects/Usecases/src/banking/batchdata.csv'
s3_key = 'bronzeraw/toprocess/customers.csv'

# Create the S3 bucket
try:
    s3.create_bucket(Bucket=bucket_name)
    print(f"Bucket '{bucket_name}' created successfully.")
except s3.exceptions.BucketAlreadyExists as e:
    print(f"Bucket '{bucket_name}' already exists.")
except s3.exceptions.BucketAlreadyOwnedByYou as e:
    print(f"Bucket '{bucket_name}' already owned by you.")

# Upload the CSV file to the S3 bucket
try:
    s3.upload_file(file_path, bucket_name, s3_key)
    print(f"File '{file_path}' uploaded successfully to bucket '{bucket_name}' as '{s3_key}'.")
except FileNotFoundError:
    print(f"The file '{file_path}' was not found.")
except NoCredentialsError:
    print("Credentials not available.")
except PartialCredentialsError:
    print("Incomplete credentials provided.")
except Exception as e:
    print(f"An error occurred: {e}")
