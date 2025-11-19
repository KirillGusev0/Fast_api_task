# -*- coding: utf-8 -*-
from fastapi import FastAPI
from starlette.middleware.base import BaseHTTPMiddleware

from routers.api_v1_router import api_v1_router
from utils.middleware import DBErrorMiddleware
from settings.settings import settings

app = FastAPI(title="FastAPI Project App")

# Middleware
app.add_middleware(BaseHTTPMiddleware, dispatch=DBErrorMiddleware())

# Routers
app.include_router(api_v1_router, prefix="/api/v1")


@app.get("/")
async def root():
    return {"message": "API is running", "debug": settings.DEBUG}
