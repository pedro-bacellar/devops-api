# DevOps API

## Description

A simple Python API built with FastAPI and containerized with Docker.

This project was developed primarily through the terminal to improve my command-line skills and practice fundamental DevOps concepts, including Python virtual environments, dependency management, containerization, and application deployment.

## How I Built It

### Part 1 — Setting Up the Environment

1. Created an empty GitHub repository.
2. Created the project directory structure.
3. Used Claude to generate a simple Python API.
4. Installed the Python package management and virtual environment tools:

   ```bash
   sudo apt install -y python3-pip python3-venv
   ```

5. Created and activated a Python virtual environment:

   ```bash
   python3 -m venv .venv
   source .venv/bin/activate
   ```

   This isolates the project's Python dependencies from the system-wide environment.

6. Installed the project dependencies:

   ```bash
   pip install fastapi uvicorn pytest httpx
   ```

7. Generated a `requirements.txt` file to record the installed Python packages and their versions:

   ```bash
   pip freeze > requirements.txt
   ```

8. Configured `.gitignore` to exclude cache files, the virtual environment, and sensitive files from version control.

### Part 2 — Containerizing the Application with Docker

1. Created a `Dockerfile` to define the application's container image.
2. Configured the image to:
   - Use `python:3.12-slim` as the base image.
   - Set up the application directory.
   - Copy `requirements.txt` into the image.
   - Install the Python dependencies.
   - Copy the application source code into the image.
   - Expose port `8000`.
   - Start the API using Uvicorn, listening on `0.0.0.0:8000`.

3. Created a `.dockerignore` file to exclude unnecessary files from the Docker build context, including cache files, `.git`, tests, and `.env` files.
4. Built the Docker image.
5. Started a container from the image and verified that the API was accessible.

## Prerequisites

- Git installed to clone the repository.
- Docker installed and running to build the image and run the container.

## Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/pedro-bacellar/devops-api.git
cd devops-api
```

### 2. Build the Docker Image

```bash
docker build -t devops-api .
```

### 3. Run the Container

```bash
docker run -d --name api -p 8000:8000 devops-api
```

The API will be available at `http://localhost:8000`.

### 4. Test the Endpoints

Check the API health:

```bash
curl http://localhost:8000/health
```

Test the addition endpoint:

```bash
curl "http://localhost:8000/soma?a=2&b=3"
```

### 5. Access the Interactive API Documentation

Open the following URL in your browser:

http://localhost:8000/docs

