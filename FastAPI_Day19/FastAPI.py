from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field

app = FastAPI(title="Task Management API")


# Professional Data Model with Strict Validation
class Task(BaseModel):
    id: int = Field(
        ...,
        gt=0,
        description="Unique task identifier; must be a positive integer."
    )
    title: str = Field(
        ...,
        min_length=3,
        max_length=50,
        description="Task title between 3 and 50 characters."
    )
    description: str | None = Field(
        default=None,
        max_length=200,
        description="Optional detailed description."
    )
    completed: bool = Field(
        default=False,
        description="Task status flag."
    )


# In-memory database initialized as a dictionary for O(1) efficiency
db_tasks: dict[int, Task] = {}


# --- API ENDPOINTS ---

@app.post(
    "/tasks/",
    response_model=Task,
    status_code=status.HTTP_201_CREATED,
    summary="Create a new task"
)
def create_task(task: Task) -> Task:
    # Handles HTTP 409 Conflict scenario
    if task.id in db_tasks:
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT,
            detail=f"Task with ID {task.id} already exists."
        )

    db_tasks[task.id] = task
    return task


@app.get(
    "/tasks/{task_id}",
    response_model=Task,
    summary="Retrieve a task by ID"
)
def get_task(task_id: int) -> Task:
    # Handles HTTP 404 Not Found scenario
    if task_id not in db_tasks:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Task with ID {task_id} was not found."
        )

    return db_tasks[task_id]