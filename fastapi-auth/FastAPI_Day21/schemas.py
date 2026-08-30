from typing import List, Optional
from pydantic import BaseModel, ConfigDict, EmailStr

# --- Task Schemas ---
class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    is_completed: bool = False

class TaskCreate(TaskBase):
    pass

class TaskRead(TaskBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)


# --- User Schemas ---
class UserBase(BaseModel):
    username: str
    email: EmailStr

class UserCreate(UserBase):
    pass

class UserRead(UserBase):
    id: int

    model_config = ConfigDict(from_attributes=True)


# --- Nested Response Schema ---
class UserWithTasksRead(UserRead):
    """Schema representing a user along with their associated tasks (Nested Schema)."""
    tasks: List[TaskRead] = []

    model_config = ConfigDict(from_attributes=True)