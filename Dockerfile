# Start from the jupyter/datascience-notebook image
FROM jupyter/datascience-notebook:latest

# Switch to the root user so we can install packages
USER root

# Install Git LFS
RUN apt-get update && \
    apt-get install -y git-lfs && \
    git lfs install

# Switch back to the jovyan user
USER jovyan
