#!/bin/sh
mlflow models serve -m mlruns/0/f58d52138c70487d901d6a99b201aeab/artifacts/hf_model_custom -h 127.0.0.1  -p 1234

