from fastapi import APIRouter

from app.dependencies import CurrentUser
from app.schemas.task import TaskCreate, TaskResponse

router = APIRouter(
    prefix="/tasks",
    tags=["Tasks"],
)

tasks: list[TaskResponse] = []


@router.post("/", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    current_user: CurrentUser,
) -> TaskResponse:
    new_task = TaskResponse(
        id=len(tasks) + 1,
        title=task.title,
        description=task.description,
    )

    tasks.append(new_task)

    return new_task


@router.get("/", response_model=list[TaskResponse])
def get_tasks(
    current_user: CurrentUser,
) -> list[TaskResponse]:
    return tasks