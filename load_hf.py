from transformers import AutoModelForSequenceClassification, AutoTokenizer
import os
import mlflow.pytorch
import torch.nn.functional as F
import torch
# Define the Custom PyFunc Model
import mlflow.pyfunc

class HuggingFaceWrapper(mlflow.pyfunc.PythonModel):
    def load_context(cls, context):
        cls.model = AutoModelForSequenceClassification.from_pretrained(context.artifacts["model"])
        cls.tokenizer = AutoTokenizer.from_pretrained(context.artifacts["tokenizer"])

    def predict(self, context, model_input):
        # Extract text data from the DataFrame
        texts = model_input["text"].tolist()

        # Tokenize
        inputs = self.tokenizer(texts, return_tensors="pt", truncation=True, padding=True)

        # Get model's outputs
        with torch.no_grad():
            outputs = self.model(**inputs).logits

        # Apply the softmax to get probabilities
        probabilities = torch.nn.functional.softmax(outputs, dim=1)

        # Get the predicted class label
        predicted_classes = probabilities.argmax(dim=1).tolist()
        
        return predicted_classes


model_name = "alexFiorenza/intent_classification_js"  # replace with your model's identifier on Hugging Face
tokenizer = AutoTokenizer.from_pretrained(model_name)
model = AutoModelForSequenceClassification.from_pretrained(model_name)

os.makedirs("hf_model", exist_ok=True)
model.save_pretrained("hf_model")
tokenizer.save_pretrained("hf_model")


with mlflow.start_run() as run:
    artifacts = {
        "model": "hf_model",
        "tokenizer": "hf_model"
    }

    model_info=mlflow.pyfunc.log_model(artifact_path="hf_model_custom",
                            python_model=HuggingFaceWrapper(),
                            artifacts=artifacts)
