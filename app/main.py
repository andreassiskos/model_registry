from fastapi import FastAPI, UploadFile, File, Form, HTTPException
from app import models, database, crud
from app.schemas import ModelMetadata
import shutil
import os
from datetime import datetime

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()


@app.post("/models")
def upload_model(
    file: UploadFile = File(...),
    name: str = Form(...),
    version: str = Form(...),
    accuracy: float = Form(...),
):
    filename = f"{name}_{version}.pkl"
    save_path = f"models/{filename}"
    os.makedirs("models", exist_ok=True)
    with open(save_path, "wb") as buffer:
        shutil.copyfileobj(file.file, buffer)

    model_data = {
        "name": name,
        "version": version,
        "accuracy": accuracy,
        "timestamp": datetime.utcnow(),
        "filepath": save_path,
    }

    crud.create_model(database.SessionLocal(), model_data)
    return {"message": "Model uploaded"}


@app.get("/models")
def list_models():
    return crud.get_all_models(database.SessionLocal())


@app.get("/models/{name}")
def get_model_by_name(name: str):
    model = crud.get_model_by_name(database.SessionLocal(), name)
    if model is None:
        raise HTTPException(status_code=404, detail="Model not found")
    return model
