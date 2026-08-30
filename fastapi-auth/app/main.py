from fastapi import FastAPI

from app.routers import tasks, users

app = FastAPI(
    title="Task Management API",
    description="A modular FastAPI application demonstrating APIRouter and Dependency Injection.",
    version="1.0.0",
)

app.include_router(users.router)
app.include_router(tasks.router)


@app.get("/")
def root() -> dict[str, str]:
    return {
        "message": "Task Management API is running."
    }