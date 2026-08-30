from fastapi import FastAPI

app = FastAPI(title="Day 17 - RESTful API")

# 1. GET endpoint - Home page
@app.get("/")
def get_home() -> dict[str, str]:
    return {"message": "Welcome to FastAPI!"}

# 2. GET endpoint - About section
@app.get("/about")
def get_about() -> dict[str, str]:
    return {"app_name": "My API", "status": "active"}

# 3. GET endpoint - User profile with dynamic parameter
@app.get("/users/{user_id}")
def get_user(user_id: int) -> dict[str, int | str]:
    return {"user_id": user_id, "role": "student"}