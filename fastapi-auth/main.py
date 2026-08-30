from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer
from pwdlib import PasswordHash
import jwt

app = FastAPI()
password_hash = PasswordHash.recommended()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")

users = {}
SECRET_KEY = "secret-key"

@app.post("/register")
def register(username: str, password: str):
    users[username] = password_hash.hash(password)
    return {"message": "Registered successfully"}

@app.post("/login")
def login(username: str, password: str):
    if username not in users or not password_hash.verify(password, users[username]):
        raise HTTPException(401, "Invalid credentials")

    token = jwt.encode({"sub": username}, SECRET_KEY, algorithm="HS256")
    return {"access_token": token, "token_type": "bearer"}

@app.get("/protected")
def protected(token: str = Depends(oauth2_scheme)):
    try:
        data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        return {"message": f"Hello {data['sub']}"}
    except:
        raise HTTPException(401, "Invalid token")