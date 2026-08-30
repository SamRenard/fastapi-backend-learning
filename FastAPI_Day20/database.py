from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase

# TODO: Replace with your actual PostgreSQL credentials
# Format: postgresql://<username>:<password>@<host>:<port>/<database_name>
SQLALCHEMY_DATABASE_URL = "postgresql://postgres:123logan@localhost:5432/fastapi_db"

# Creating the engine
engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True)

# Session factory for handling database transactions
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for SQLAlchemy models (SQLAlchemy 2.0 style)
class Base(DeclarativeBase):
    pass

# Dependency to get a database session per request
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()