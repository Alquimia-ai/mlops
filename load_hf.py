from transformers import AutoModelForSequenceClassification, AutoTokenizer
import os
import mlflow.pytorch


model_name = "alexFiorenza/intent_classification_js"  # replace with your model's identifier on Hugging Face
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

os.makedirs("hf_model", exist_ok=True)
model.save_pretrained("hf_model")
tokenizer.save_pretrained("hf_model")


# Start an MLflow run and log the model
with mlflow.start_run() as run:
    mlflow.pytorch.log_model(model, "model", registered_model_name="intent_classification_js")