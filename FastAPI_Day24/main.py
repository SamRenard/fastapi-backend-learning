import time
import logging
import asyncio
from fastapi import FastAPI, Request, HTTPException, Depends

# 1. Professional Logging Setup
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger("api_logger")

app = FastAPI(title="Day 24: FastAPI Architecture")


# 2. Logging Middleware
@app.middleware("http")
async def log_requests(request: Request, call_next):
    start_time = time.time()
    response = await call_next(request)
    process_time = time.time() - start_time

    logger.info(
        f"Method: {request.method} | Path: {request.url.path} | "
        f"Status: {response.status_code} | Time: {process_time:.4f}s"
    )
    return response


# 3. Simple In-Memory Rate Limiter (Max 5 requests per 60 seconds)
RATE_LIMIT = 5
TIME_WINDOW = 60
client_requests = {}


async def rate_limit_dependency(request: Request):
    client_ip = request.client.host
    current_time = time.time()

    if client_ip not in client_requests:
        client_requests[client_ip] = []

    # Remove old requests outside the time window
    client_requests[client_ip] = [
        req_time for req_time in client_requests[client_ip]
        if current_time - req_time < TIME_WINDOW
    ]

    if len(client_requests[client_ip]) >= RATE_LIMIT:
        logger.warning(f"Rate limit exceeded for IP: {client_ip}")
        raise HTTPException(status_code=429, detail="Too Many Requests")

    client_requests[client_ip].append(current_time)


# 4. Async Endpoint Refactor (Simulating async I/O work)
@app.get("/api/v1/users", dependencies=[Depends(rate_limit_dependency)])
async def get_users_async():
    """
    Refactored endpoint: Uses async/await to prevent blocking the event loop.
    """
    await asyncio.sleep(1)  # Simulates async DB fetch (e.g., SQLAlchemy 2.0 async call)
    return {
        "status": "success",
        "message": "Async data fetched successfully",
        "data": [{"id": 1, "username": "admin"}]
    }