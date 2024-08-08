from fastapi import FastAPI
from .database import engine
from .models.models import Base

app = FastAPI()

# Base.metadata.create_all(bind=engine)
