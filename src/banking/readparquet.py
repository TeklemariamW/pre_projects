import pyarrow.parquet as pq

# Load Parquet file from S3
s3_path = "s3://banktekle/silverstaging/removed_duplicates/"
table = pq.read_table(s3_path)

# Display schema and sample data
print(table.schema)
print(table.to_pandas().head())
