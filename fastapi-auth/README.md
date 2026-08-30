# FastAPI Authentication API

Simple authentication API built with FastAPI.

## Features
- User registration
- Password hashing with Argon2
- JWT authentication
- Protected endpoint

## Run

```bash
pip install fastapi uvicorn pyjwt pwdlib[argon2]
uvicorn main:app --reload