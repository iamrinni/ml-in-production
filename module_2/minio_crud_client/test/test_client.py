from minio import Minio

client = Minio(
    "127.0.0.1:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

def create_bucket(bucket_name: str):
    if not client.bucket_exists(bucket_name):
        client.make_bucket(bucket_name)
    print(f"Bucket '{bucket_name}' created or already exists")

create_bucket("test")
