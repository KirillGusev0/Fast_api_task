# -*- coding: utf-8 -*-
# apps/auth/schemas.py
from pydantic import BaseModel, Field
from typing import Optional


class RegisterUser(BaseModel):
    name: str = Field(min_length=1)
    username: str = Field(min_length=1)
    password: str = Field(min_length=1)
    email: Optional[str] = None


class LoginUser(BaseModel):
    username: str = Field(min_length=1)
    password: str = Field(min_length=1)


class TokenPair(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"
