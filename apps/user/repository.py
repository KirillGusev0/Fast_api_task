# -*- coding: utf-8 -*-
# apps/user/repository.py
from typing import List, Optional
from sqlalchemy import select, update, delete
from sqlalchemy.ext.asyncio import AsyncSession
from apps.user.models import User


class UserRepository:
   

    async def create(self, db: AsyncSession, user: User) -> User:
        """
        SQL:
        INSERT INTO users (name, username, hashed_password, email, created_at)
        VALUES (:name, :username, :hashed_password, :email, now())
        RETURNING *;
        """
        db.add(user)
        await db.commit()
        await db.refresh(user)
        return user

    async def create_many(self, db: AsyncSession, users: List[User]) -> List[User]:
        """
        SQL:
        INSERT INTO users (name, username, hashed_password, email)
        VALUES (...), (...), ...;
        """
        
        for u in users:
            db.add(u)
        try:
            await db.commit()
        except Exception:
            await db.rollback()
            raise
        for u in users:
            await db.refresh(u)
        return users

    async def get_all(self, db: AsyncSession) -> List[User]:
        """
        SQL:
        SELECT id, name, username, email, created_at FROM users;
        """
        result = await db.execute(select(User))
        return result.scalars().all()

    async def get_by_id(self, db: AsyncSession, user_id: int) -> Optional[User]:
        """
        SQL:
        SELECT * FROM users WHERE id = :user_id;
        """
        result = await db.execute(select(User).where(User.id == user_id))
        return result.scalars().first()

    async def get_by_ids(self, db: AsyncSession, ids: List[int]) -> List[User]:
        """
        SQL:
        SELECT * FROM users WHERE id IN (:ids...);
        """
        result = await db.execute(select(User).where(User.id.in_(ids)))
        return result.scalars().all()

    async def get_by_username(self, db: AsyncSession, username: str) -> Optional[User]:
        """
        SQL:
        SELECT * FROM users WHERE username = :username LIMIT 1;
        """
        result = await db.execute(select(User).where(User.username == username))
        return result.scalars().first()

    async def update(self, db: AsyncSession, user_id: int, data: dict) -> Optional[User]:
        """
        SQL:
        UPDATE users SET col1 = :val1, ... WHERE id = :user_id RETURNING *;
        """
        user = await self.get_by_id(db, user_id)
        if not user:
            return None
        for k, v in data.items():
            if k == "password":
               
                continue
            if hasattr(user, k):
                setattr(user, k, v)
        try:
            await db.commit()
            await db.refresh(user)
            return user
        except Exception:
            await db.rollback()
            raise

    async def delete(self, db: AsyncSession, user_id: int) -> Optional[User]:
        """
        SQL:
        DELETE FROM users WHERE id = :user_id RETURNING *;
        """
        user = await self.get_by_id(db, user_id)
        if not user:
            return None
        await db.delete(user)
        await db.commit()
        return user
