from sqlalchemy import Column, String, Float, DateTime
from .database import Base


class ModelRegistry(Base):
    __tablename__ = "models"

    name = Column(String, primary_key=True)
    version = Column(String)
    accuracy = Column(Float)
    timestamp = Column(DateTime)
    filepath = Column(String)
