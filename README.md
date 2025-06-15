# 🧠 Model Registry API

A lightweight model registry system built with FastAPI, PostgreSQL, and Docker. This system allows uploading and retrieving metadata for machine learning models.

## 🚀 Features

- Upload ML models (`.pkl`) with metadata: name, version, accuracy
- Retrieve all registered models or specific ones by name
- RESTful API with FastAPI
- PostgreSQL database with SQLAlchemy ORM
- Dockerized setup for local development
- CI/CD pipeline using GitHub Actions
- Logs saved to files (API logs and test logs)

---

## 📁 Project Structure

```
.
├── app/
│   ├── main.py            # FastAPI app and routes
│   ├── database.py        # DB connection setup
│   ├── models.py          # SQLAlchemy model
│   ├── crud.py            # DB CRUD operations
│   ├── schemas.py         # Pydantic schemas
├── test/
│   └── test_api.py        # Pytest for API endpoints
├── logs/                  # Stores test and API logs
├── models/                # Uploaded model files
├── Dockerfile             # App Dockerfile
├── docker-compose.yaml    # Multi-service setup
├── requirements.txt       # Python dependencies
└── .github/
    └── workflows/
        └── ci.yml         # GitHub Actions workflow
```

---

## 🔧 Setup Instructions

### 🐳 Run with Docker (Recommended)

1. **Clone the repo**

```bash
git clone https://github.com/andreassiskos/model-registry.git
cd model-registry
```

2. **Build and run the app**

```bash
docker-compose up --build
```

- API: [http://localhost:8000](http://localhost:8000)
- Swagger UI: [http://localhost:8000/docs](http://localhost:8000/docs)

---

## 🧪 Running Tests

Tests are executed inside the model_registry_web container.

```bash
docker ps -a
docker exec -it <model_registry_web-container-id> bash
pytest test
```

---

## 🔁 API Endpoints

### ➕ Upload Model

**POST** `/models`

Upload a `.pkl` file with metadata.

**Form Data:**

- `file`: model file
- `name`: model name
- `version`: model version
- `accuracy`: model accuracy

```bash
curl -X POST http://localhost:8000/models \
  -F "file=@dummy_model.pkl" \
  -F "name=MyModel" \
  -F "version=1.0" \
  -F "accuracy=0.95"
```

---

### 📄 List All Models

**GET** `/models`

```bash
curl http://localhost:8000/models
```

---

### 🔍 Get Model by Name

**GET** `/models/{name}`

```bash
curl http://localhost:8000/models/MyModel
```

---

## ⚙️ CI/CD Pipeline (GitHub Actions)

Every `push` to any branch:

- Starts a PostgreSQL service
- Installs dependencies
- Runs unit tests with `pytest`
- Archives logs (`logs/test_results.log`, `logs/api.log`)

See `.github/workflows/ci.yml` for full configuration.

---

## 🧰 Tech Stack

- Python 3.10
- FastAPI
- PostgreSQL 14
- SQLAlchemy
- Docker & Docker Compose
- GitHub Actions
- Pytest + HTTPX

---
