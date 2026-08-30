# Task Management API

A modular REST API built with FastAPI.

This project demonstrates a clean FastAPI architecture using
APIRouter and Dependency Injection.

## Features

- Modular API routing with APIRouter
- Dependency Injection with Depends
- Pydantic data validation
- Automatic API documentation
- Professional project structure
- Type hints
- Separation of concerns

## Project Structure

```text
fastapi-project/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── dependencies.py
│   │
│   ├── routers/
│   │   ├── __init__.py
│   │   ├── users.py
│   │   └── tasks.py
│   │
│   └── schemas/
│       ├── __init__.py
│       ├── user.py
│       └── task.py
│
├── README.md
├── requirements.txt
└── .gitignore