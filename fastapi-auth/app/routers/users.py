from fastapi import APIRouter

from app.schemas.user import UserCreate, UserResponse

router = APIRouter(
    prefix="/users",
    tags=["Users"],
)

users: list[UserResponse] = []


@router.post("/", response_model=UserResponse)
def create_user(user: UserCreate) -> UserResponse:
    new_user = UserResponse(
        id=len(users) + 1,
        name=user.name,
        email=user.email,
    )

    users.append(new_user)

    return new_user


@router.get("/", response_model=list[UserResponse])
def get_users() -> list[UserResponse]:
    return users