```sh
export CR_PAT=YOUR_TOKEN # Github token
echo $CR_PAT | docker login ghcr.io -u USERNAME --password-stdin
docker pull ghcr.io/mlflow/mlflow
```

Call endpoint with curl

```sh
curl http://127.0.0.1:1234/invocations -H 'Content-Type: application/json' -d '{
  "dataframe_records": [
    {"text": "Do you have availability?"},{"text":"Which is my Dog name?"}
  ]
}'
```

### Last stable version run is

runs:/f58d52138c70487d901d6a99b201aeab/hf_model_custom
