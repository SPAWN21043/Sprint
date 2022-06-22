import os
from os.path import join, dirname

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, DeclarativeMeta
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())
login = os.getenv("FSTR_DB_LOGIN")
password = os.getenv("FSTR_DB_PASS")
host = os.getenv("FSTR_DB_HOST")
port = os.getenv("FSTR_DB_PORT")
name = os.getenv("FSTR_DB_NAME")

SQLALCHEMY_DATABASE_URL = f"postgresql://{login}:{password}@{host}/{name}"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base: DeclarativeMeta = declarative_base()
