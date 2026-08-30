# FastAPI Day 24: Core Architecture 🚀

## Overview
This repository contains the practical implementation of FastAPI core architectural components, focusing on performance, monitoring, and security.

## Features Implemented
*   **Logging Middleware**: Intercepts HTTP requests to calculate and log processing time, status codes, and routing paths.
*   **Rate Limiting**: Custom dependency-based rate limiter to protect endpoints from spam (5 req/min).
*   **Async Refactoring**: Fully non-blocking asynchronous endpoints utilizing `async/await` for optimized I/O operations.

## Quick Start
```bash
# Install dependencies
pip install fastapi uvicorn

# Run the server
uvicorn main:app --reload# FastAPI Day 24: Core Architecture 🚀

## Overview
This repository contains the practical implementation of FastAPI core architectural components, focusing on performance, monitoring, and security.

## Features Implemented
*   **Logging Middleware**: Intercepts HTTP requests to calculate and log processing time, status codes, and routing paths.
*   **Rate Limiting**: Custom dependency-based rate limiter to protect endpoints from spam (5 req/min).
*   **Async Refactoring**: Fully non-blocking asynchronous endpoints utilizing `async/await` for optimized I/O operations.

## Quick Start
```bash
# Install dependencies
pip install fastapi uvicorn

# Run the server
uvicorn main:app --reload