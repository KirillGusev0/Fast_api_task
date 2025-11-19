# -*- coding: utf-8 -*-
from typing import Optional
from sqlalchemy.ext.asyncio import AsyncSession

from apps.auth.repository import AuthRepository
from apps.auth.schemas import RegisterUser, LoginUser, TokenPair

from utils.jwt import (
    create_access_token,
    create_refresh_token,
    decode_token
)


class AuthService:
    def __init__(self):
        self.repo = AuthRepository()

    async def register(self, db: AsyncSession, data: RegisterUser):
        return await self.repo.register_user(db, data)

    async def login(self, db: AsyncSession, data: LoginUser) -> Optional[TokenPair]:
        user = await self.repo.authenticate_user(db, data)
        if not user:
            return None

        token_data = {"sub": user.username, "user_id": user.id}

        access = create_access_token(token_data)
        refresh = create_refresh_token(token_data)

        return TokenPair(access_token=access, refresh_token=refresh)

    async def refresh(self, refresh_token: str) -> Optional[TokenPair]:
        payload = decode_token(refresh_token)
        if not payload:
            return None

        
        if payload.get("type") != "refresh":
            return None

        token_data = {
            "sub": payload.get("sub"),
            "user_id": payload.get("user_id"),
        }

        access = create_access_token(token_data)
        refresh = create_refresh_token(token_data)

        return TokenPair(access_token=access, refresh_token=refresh)

