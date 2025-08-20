import psycopg2
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

from app.config import settings


engine = create_engine(settings.DATABASE_URL, echo=True) # echo=True shows SQL in logs
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_connection():
    return psycopg2.connect(settings.DATABASE_URL)
