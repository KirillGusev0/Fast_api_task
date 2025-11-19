# -*- coding: utf-8 -*-
# apps/user/routers.py
from fastapi import APIRouter, Depends, HTTPException, status
from typing import List
from sqlalchemy.ext.asyncio import AsyncSession

from db.database import get_db
from apps.user.schemas import UserCreate, UserRead, UserUpdate
from apps.user.services import UserService

router = APIRouter(tags=["users"])
service = UserService()


@router.post("/", response_model=UserRead, status_code=status.HTTP_201_CREATED)
async def create_user(user: UserCreate, db: AsyncSession = Depends(get_db)):
    
    created = await service.create_user(db, user)
    return created


@router.post("/bulk", response_model=List[UserRead], status_code=status.HTTP_201_CREATED)
async def create_users_bulk(users: List[UserCreate], db: AsyncSession = Depends(get_db)):
    created = await service.create_many(db, users)
    return created


@router.get("/", response_model=List[UserRead])
async def list_users(db: AsyncSession = Depends(get_db)):
    return await service.get_all(db)


@router.get("/ids", response_model=List[UserRead])
async def get_users_by_ids(ids: str, db: AsyncSession = Depends(get_db)):
    
    try:
        id_list = [int(x) for x in ids.split(",") if x.strip()]
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid ids format")
    users = await service.get_by_ids(db, id_list)
    return users


@router.get("/{user_id}", response_model=UserRead)
async def get_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await service.get_by_id(db, user_id)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.put("/{user_id}", response_model=UserRead)
async def update_user(user_id: int, payload: UserUpdate, db: AsyncSession = Depends(get_db)):
    updated = await service.update_user(db, user_id, payload)
    if not updated:
        raise HTTPException(status_code=404, detail="User not found")
    return updated


@router.delete("/{user_id}", response_model=UserRead)
async def delete_user(user_id: int, db: AsyncSession = Depends(get_db)):
    deleted = await service.delete_user(db, user_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted
