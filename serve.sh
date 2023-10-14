#!/bin/sh
mlflow models serve -m mlruns/0/5bd4c25a72c34cc599305a5ade5c4b29/artifacts/hf_model_custom -h 127.0.0.1  -p 1234

