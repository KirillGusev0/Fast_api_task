# -*- coding: utf-8 -*-
# apps/user/services.py
from typing import List, Optional
from passlib.hash import bcrypt
from sqlalchemy.ext.asyncio import AsyncSession
from apps.user.repository import UserRepository
from apps.user.schemas import UserCreate, UserUpdate
from apps.user.models import User


class UserService:
    def __init__(self):
        self.repo = UserRepository()

    async def create_user(self, db: AsyncSession, data: UserCreate) -> User:
        hashed = bcrypt.hash(data.password)
        user = User(
            name=data.name,
            username=data.username,
            hashed_password=hashed,
            email=data.email
        )
        return await self.repo.create(db, user)

    async def create_many(self, db: AsyncSession, data_list: List[UserCreate]) -> List[User]:
        users = []
        for d in data_list:
            users.append(
                User(
                    name=d.name,
                    username=d.username,
                    hashed_password=bcrypt.hash(d.password),
                    email=d.email
                )
            )
        return await self.repo.create_many(db, users)

    async def get_all(self, db: AsyncSession) -> List[User]:
        return await self.repo.get_all(db)

    async def get_by_id(self, db: AsyncSession, user_id: int) -> Optional[User]:
        return await self.repo.get_by_id(db, user_id)

    async def get_by_ids(self, db: AsyncSession, ids: List[int]) -> List[User]:
        return await self.repo.get_by_ids(db, ids)

    async def update_user(self, db: AsyncSession, user_id: int, payload: UserUpdate) -> Optional[User]:
        data = payload.dict(exclude_unset=True)
        
        if "password" in data:
            data_pop = data.pop("password")
            hashed = bcrypt.hash(data_pop)
            
            data["hashed_password"] = hashed
        return await self.repo.update(db, user_id, data)

    async def delete_user(self, db: AsyncSession, user_id: int) -> Optional[User]:
        return await self.repo.delete(db, user_id)

        