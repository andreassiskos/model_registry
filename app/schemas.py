from pydantic import BaseModel
from datetime import datetime


class ModelMetadata(BaseModel):
    name: str
    version: str
    accuracy: float
    timestamp: datetime
    filepath: str
