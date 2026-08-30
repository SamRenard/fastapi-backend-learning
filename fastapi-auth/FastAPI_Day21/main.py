from contextlib import asynccontextmanager
from typing import List
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.future import select
from sqlalchemy.orm import selectinload

from database import engine, Base, get_db
import models
import schemas


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Initialize database tables on application startup
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(
    title="RESTful FastAPI Architecture - Day 21",
    description="Implementation of One-to-Many ORM relationships with Pydantic nested response models.",
    version="1.0.0",
    lifespan=lifespan
)


@app.post("/users/", response_model=schemas.UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user: schemas.UserCreate, db: AsyncSession = Depends(get_db)):
    """Create a new user."""
    db_user = models.User(username=user.username, email=user.email)
    db.add(db_user)
    await db.commit()
    await db.refresh(db_user)
    return db_user


@app.post("/users/{user_id}/tasks/", response_model=schemas.TaskRead, status_code=status.HTTP_201_CREATED)
async def create_task_for_user(
        user_id: int,
        task: schemas.TaskCreate,
        db: AsyncSession = Depends(get_db)
):
    """Create a task assigned to a specific user."""
    result = await db.execute(select(models.User).where(models.User.id == user_id))
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    db_task = models.Task(**task.model_dump(), user_id=user_id)
    db.add(db_task)
    await db.commit()
    await db.refresh(db_task)
    return db_task


@app.get("/users/{user_id}", response_model=schemas.UserWithTasksRead)
async def get_user_with_tasks(user_id: int, db: AsyncSession = Depends(get_db)):
    """
    Fetch a single user with all associated tasks.
    Uses selectinload() to avoid MissingGreenlet async lazy-loading exceptions.
    """
    stmt = (
        select(models.User)
        .options(selectinload(models.User.tasks))
        .where(models.User.id == user_id)
    )
    result = await db.execute(stmt)
    user = result.scalar_one_or_none()

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return user