```sh
export CR_PAT=YOUR_TOKEN # Github token
echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin
docker pull ghcr.io/mlflow/mlflow
```
