import os

MINIO_CONFIG = {
    "endpoint": os.getenv("MINIO_ENDPOINT", "127.0.0.1:9000"),
    "access_key": os.getenv("MINIO_ACCESS_KEY", "minioadmin"),
    "secret_key": os.getenv("MINIO_SECRET_KEY", "minioadmin"),
    "secure": os.getenv("MINIO_SECURE", "false").lower() == "true",
}