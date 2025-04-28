from minio import Minio
from config import MINIO_CONFIG


class MinioClient:
    def __init__(self):
        self.client = Minio(
            MINIO_CONFIG["endpoint"],
            access_key=MINIO_CONFIG["access_key"],
            secret_key=MINIO_CONFIG["secret_key"],
            #secure=MINIO_CONFIG["secure"],
        )

    def create_bucket(self, bucket_name: str):
        if not self.client.bucket_exists(bucket_name):
            self.client.make_bucket(bucket_name)

    def upload_file(self, bucket_name: str, object_name: str, file_path: str):
        self.create_bucket(bucket_name)
        self.client.fput_object(bucket_name, object_name, file_path)

    def download_file(self, bucket_name: str, object_name: str, file_path: str):
        self.client.fget_object(bucket_name, object_name, file_path)

    def delete_file(self, bucket_name: str, object_name: str):
        self.client.remove_object(bucket_name, object_name)

    def get_metadata(self, bucket_name: str, object_name: str):
        return self.client.stat_object(bucket_name, object_name)
