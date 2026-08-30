from typing import Annotated

from fastapi import Depends


def get_current_user() -> dict:
    """
    Return the currently authenticated user.

    This function is used as a dependency and can later
    be replaced with real authentication logic.
    """
    return {
        "id": 1,
        "name": "Demo User",
        "email": "demo@example.com",
    }


CurrentUser = Annotated[dict, Depends(get_current_user)]