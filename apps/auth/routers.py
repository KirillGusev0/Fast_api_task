# -*- coding: utf-8 -*-

# apps/auth/routers.py
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_db
from apps.auth.schemas import RegisterUser, LoginUser, TokenPair
from apps.auth.services import AuthService
from apps.user.schemas import UserRead

router = APIRouter(tags=["auth"])
service = AuthService()


@router.post("/register", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def register_user(data: RegisterUser, db: AsyncSession = Depends(get_db)):
    try:
        user = await service.register(db, data)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))
    return user


@router.post("/login", response_model=TokenPair)
async def login_user(data: LoginUser, db: AsyncSession = Depends(get_db)):
    token_pair = await service.login(db, data)
    if not token_pair:
        raise HTTPException(status_code=400, detail="Invalid credentials")
    return token_pair


@router.post("/refresh", response_model=TokenPair)
async def refresh_token(payload: dict):
    
    refresh = payload.get("refresh_token")
    if not refresh:
        raise HTTPException(status_code=400, detail="Missing refresh_token")
    pair = await service.refresh(refresh)
    if not pair:
        raise HTTPException(status_code=401, detail="Invalid refresh token")
    return pair
