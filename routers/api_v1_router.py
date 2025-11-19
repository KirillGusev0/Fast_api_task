# -*- coding: utf-8 -*-
from fastapi import APIRouter

from apps.user.routers import router as user_router
from apps.auth.routers import router as auth_router
from apps.project.routers import router as project_router

api_v1_router = APIRouter()

api_v1_router.include_router(user_router)
api_v1_router.include_router(auth_router)
api_v1_router.include_router(project_router)
