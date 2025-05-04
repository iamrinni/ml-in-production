***
# Minio

## For local run

```bash
cd minio_crud_client
poetry install
```

## Minio, Local with Docker setup

docker-compose.yml	- For local development with Docker 

minio-deployment.yaml	For deploying to Kubernetes 

### Local with Docker:

```bash
```docker compose up -d```

Then you can login to minio using UI:

And test bucket creation using:

```poetry run python test_client.py ```
(creates a 'test' bucket)


## Kubernetes setup

Start kubernetes cluster

```minikube start ```

```bash
kubectl apply -f minio-deployment.yaml
kubectl apply -f minio-service.yaml   

minikube service minio --url

#gives urls
```
to test  MiniO with kubernetes (using url from previous command):

http://127.0.0.1:59447 

Run k9s

```bash
k9s -A
```

Test:
```poetry run python test_kube.py ```
✅ Bucket 'test-k8s' created
✅ File uploaded
✅ File downloaded
🧾 Downloaded file content: Hello from Kubernetes MinIO!


Cloud cluster: 
```bash

kubectl port-forward service/minio 9000:9000 9001:9001
```
