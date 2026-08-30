# FastAPI RESTful Architecture - Day 21: ORM Relationships & Nested Schemas

A professional implementation of a RESTful API built with **FastAPI**, **SQLAlchemy 2.0 (Async)**, and **Pydantic v2**. This project demonstrates setting up One-to-Many relational models, avoiding async lazy-loading pitfalls using eager loading (`selectinload`), and serving structured data via nested response schemas.

---

## 🚀 Features

- **Asynchronous Database Access:** Powered by `SQLAlchemy 2.0` and `aiosqlite`.
- **Relational Data Modeling:** One-to-Many dynamic mapping between `User` and `Task` entities.
- **Nested Serialization:** Pydantic v2 schemas configured with `from_attributes=True` to format nested JSON responses seamlessly.
- **Performance Optimized:** Uses `selectinload()` strategy to eliminate N+1 query problems and prevent `MissingGreenlet` async runtime crashes.

---

## 🛠 Tech Stack

- **Framework:** FastAPI
- **ORM:** SQLAlchemy 2.0 (Async Mode)
- **Data Validation:** Pydantic v2
- **Database Driver:** `aiosqlite` (SQLite Async Engine)

---

## 📁 Project Structure

```text
.
├── database.py       # Async engine, sessionmaker, and dependency injection setup
├── models.py         # SQLAlchemy ORM database models (User, Task)
├── schemas.py        # Pydantic schemas for request validation & nested responses
├── main.py           # Application endpoints & lifecycle configuration
└── README.md         # Project documentation 