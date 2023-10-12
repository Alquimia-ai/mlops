# Use the official MLflow image as a base image
FROM ghcr.io/mlflow/mlflow


# Install dependencies required for pyenv and python build
RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    zlib1g-dev \
    libbz2-dev \
    libreadline-dev \
    libsqlite3-dev \
    wget \
    curl \
    llvm \
    libncurses5-dev \
    libncursesw5-dev \
    xz-utils \
    tk-dev \
    libffi-dev \
    liblzma-dev \
    git

# Install pyenv
RUN curl https://pyenv.run | bash

# Add pyenv to PATH
ENV PYENV_ROOT /root/.pyenv
ENV PATH $PYENV_ROOT/shims:$PYENV_ROOT/bin:$PATH

# Use pyenv to install a specific version of Python (e.g., 3.9.1) and set it as default
RUN pyenv install 3.11.5
RUN pyenv global 3.11.5


# Copy the requirements file into the container
COPY requirements.txt requirements.txt

# Install the Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Set the working directory
WORKDIR /app

# Copy your 'mlruns/' directory into the Docker image
COPY mlruns/ mlruns/
COPY serve.sh serve.sh

# When the container starts, it should run your 'serve.sh' script to start the model server
CMD ["sh", "serve.sh"]
