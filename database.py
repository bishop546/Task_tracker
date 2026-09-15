from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# This creates a local SQLite file named 'task_tracker.db'
SQLALCHEMY_DATABASE_URL = "sqlite:///./task_tracker.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    pass