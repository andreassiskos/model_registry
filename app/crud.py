from .models import ModelRegistry
from sqlalchemy.orm import Session


def create_model(db: Session, model_data: dict):
    db_model = ModelRegistry(**model_data)
    db.add(db_model)
    db.commit()


def get_all_models(db: Session):
    return db.query(ModelRegistry).all()


def get_model_by_name(db: Session, name: str):
    return db.query(ModelRegistry).filter(ModelRegistry.name == name).first()
