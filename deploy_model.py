import mlflow


client = mlflow.tracking.MlflowClient()

# Name of the registered model
model_name = "intent_classification_js"

# Version of the model you want to transition (you might need to check this)
version = 1 

client.transition_model_version_stage(
    name=model_name,
    version=version,
    stage="Production"
)
