# FastAPI PostgreSQL CRUD API

A professional, minimal RESTful API built with FastAPI and SQLAlchemy 2.0, demonstrating a clean architecture for database connectivity and CRUD operations using PostgreSQL.

## Tech Stack
* **Framework:** FastAPI
* **ORM:** SQLAlchemy 2.0
* **Database:** PostgreSQL
* **Data Validation:** Pydantic

## Project Structure
```text
.
├── database.py    # Database connection and session management
├── models.py      # SQLAlchemy 2.0 declarative models
├── schemas.py     # Pydantic models for request/response validation
├── main.py        # FastAPI application and CRUD endpoints
└── README.md      # Project documentation