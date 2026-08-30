from fastapi import FastAPI, HTTPException, Path, Query
from pydantic import BaseModel, Field
from typing import List, Optional

app = FastAPI(
    title="Tasks API",
    description="A simple, in-memory CRUD API for task management.",
    version="1.0.0"
)

# --- Pydantic Models (Validasiya üçün) ---
class TaskBase(BaseModel):
    title: str = Field(..., min_length=3, max_length=50, description="Title of the task")
    description: Optional[str] = Field(None, max_length=200)
    is_completed: bool = False

class Task(TaskBase):
    id: int

class TaskUpdate(BaseModel):
    title: Optional[str] = Field(None, min_length=3, max_length=50)
    description: Optional[str] = Field(None, max_length=200)
    is_completed: Optional[bool] = None

# --- In-Memory Database ---
tasks_db: List[Task] = []
task_id_counter = 1

# --- Endpoints (CRUD) ---

# CREATE (POST)
@app.post("/tasks/", response_model=Task, status_code=201)
def create_task(task: TaskBase):
    global task_id_counter
    new_task = Task(id=task_id_counter, **task.model_dump())
    tasks_db.append(new_task)
    task_id_counter += 1
    return new_task

# READ ALL (GET) - Query parametrləri ilə (limit, skip)
@app.get("/tasks/", response_model=List[Task])
def get_tasks(skip: int = Query(0, ge=0), limit: int = Query(10, le=100)):
    return tasks_db[skip : skip + limit]

# READ ONE (GET) - Path parametri ilə
@app.get("/tasks/{task_id}", response_model=Task)
def get_task(task_id: int = Path(..., gt=0)):
    for task in tasks_db:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

# UPDATE (PUT)
@app.put("/tasks/{task_id}", response_model=Task)
def update_task(task_update: TaskUpdate, task_id: int = Path(..., gt=0)):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            update_data = task_update.model_dump(exclude_unset=True)
            updated_task = task.model_copy(update=update_data)
            tasks_db[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

# DELETE
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int = Path(..., gt=0)):
    for index, task in enumerate(tasks_db):
        if task.id == task_id:
            tasks_db.pop(index)
            return
    raise HTTPException(status_code=404, detail="Task not found")
