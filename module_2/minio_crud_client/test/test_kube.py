from minio import Minio
from minio.error import S3Error

client = Minio(
    "localhost:9000",
    access_key="minioadmin",
    secret_key="minioadmin",
    secure=False
)

def test_minio_k8s():
    try:
        bucket_name = "test-k8s"

        if not client.bucket_exists(bucket_name):
            client.make_bucket(bucket_name)
            print(f"✅ Bucket '{bucket_name}' created")
        else:
            print(f"ℹ️ Bucket '{bucket_name}' already exists")

        # Create a test file
        with open("test_file.txt", "w") as f:
            f.write("Hello from Kubernetes MinIO!")

        client.fput_object(bucket_name, "test_file.txt", "test_file.txt")
        print("✅ File uploaded")

        client.fget_object(bucket_name, "test_file.txt", "downloaded_file.txt")
        print("✅ File downloaded")

        with open("downloaded_file.txt", "r") as f:
            content = f.read()
            print(f"🧾 Downloaded file content: {content}")

    except S3Error as e:
        print(f"❌ S3Error: {e}")

if __name__ == "__main__":
    test_minio_k8s()
