# 05-Deployment: Churn Prediction Service

## Project Overview
This Project is part of ML Zoomcamp and This folder contains a complete deployment pipeline for a customer churn prediction service. It includes model files, inference and service scripts, Docker integration, configuration for production deployment, and homework material.

***

## Directory Structure

- `.python-version`  
  Specifies the Python version used (3.12).

- `pyproject.toml`  
  Project config and dependencies:  
  - Main dependencies: `fastapi`, `scikit-learn`, `unicorn`, `uvicorn`  
  - Python requirement: `>=3.12`  
  - Development dependencies: `requests`

- `Dockerfile`  
  Multi-stage build for deploying the inference API service.  
  - Uses python:3.13.5-slim  
  - Integrates `uv` package manager  
  - Sets up venv and installs dependencies  
  - Exposes port 9696 for FastAPI service

- `.dockerignore`  
  Excludes unnecessary files/folders from Docker build (`.venv/**`, `.git`, `fly.toml`)

- `predict.py`  
  FastAPI application for churn prediction via a `/predict` endpoint.  
  - Uses serialized pipeline from `model.bin`  
  - Defines `Customer` and `PredictResponse` schema

- `main.py`  
  Entry point script, prints greeting message.

- `churn-service.py`  
  Example client for sending requests to the `/predict` endpoint and printing results.

- `fly.toml`  
  Configuration for deploying the API to Fly.io cloud platform.

- `homework.ipynb`  
  Jupyter notebook containing homework exercises, code examples, and project explanations.

- `model.bin` and `pipeline_v1.bin`  
  Serialized machine learning model pipeline files for inference.

- `uv.lock`  
  Lock file for reproducible dependency installs.

***

## Quick Start: Running the API Locally

1. **Clone the repository and navigate to the folder:**
   ```bash
   git clone https://github.com/AhmedMostafa167/ml-zoomcamp.git
   cd ml-zoomcamp/05-deployment
   ```

2. **Create and activate a Python 3.12+ virtual environment:**
   ```bash
   python3.12 -m venv .venv
   source .venv/bin/activate
   ```

3. **Install dependencies with uv:**
   ```bash
   uv sync --locked
   ```

4. **Start the API service:**
   ```bash
   uvicorn predict:app --host 0.0.0.0 --port 9696
   ```

5. **Test with an example client:**
   ```bash
   python churn-service.py
   ```

***

## Docker Deployment

To build and run the API server with Docker:

```bash
docker build -t churn-prediction:latest .
docker run -p 9696:9696 churn-prediction:latest
```

***

## Production Deployment (Fly.io)

1. Install [flyctl](https://fly.io/docs/hands-on/install-flyctl/)
2. Deploy using the provided `fly.toml` configuration:
   ```bash
   flyctl launch
   ```

***

## File Purpose Reference

| File                | Description                                  |
|---------------------|----------------------------------------------|
| `.python-version`   | Specifies Python version                     |
| `pyproject.toml`    | Project dependencies/config                  |
| `Dockerfile`        | Automated build for API container            |
| `.dockerignore`     | Build exclusions                             |
| `predict.py`        | Core API logic for predictions               |
| `main.py`           | Script entry point (utility)                 |
| `churn-service.py`  | Example client for predictions               |
| `fly.toml`          | Fly.io deployment config                     |
| `homework.ipynb`    | Assignment notebook                          |
| `model.bin`, `pipeline_v1.bin` | ML pipeline objects               |
| `uv.lock`           | Dependency lock                              |

***

## Notes

- *Models must be present in the folder to run predictions.*
- *Edit `fly.toml` before deploying to change configuration details if needed.*

***

Feel free to copy, edit, or expand this README template as your project evolves!

[1](https://github.com/AhmedMostafa167/ml-zoomcamp/blob/main/05-%20deployment/homework.ipynb)
[2](https://github.com/AhmedMostafa167/ml-zoomcamp/tree/main/05-%20deployment)
