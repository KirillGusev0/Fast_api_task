# -*- coding: utf-8 -*-
# apps/user/schemas.py
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime


class UserCreate(BaseModel):
    name: str = Field(min_length=1)
    username: str = Field(min_length=1)
    password: str = Field(min_length=1)
    email: Optional[EmailStr] = None


class UserUpdate(BaseModel):
    name: Optional[str] = None
    username: Optional[str] = None
    password: Optional[str] = None
    email: Optional[EmailStr] = None


class UserRead(BaseModel):
    id: int
    name: str
    username: str
    email: Optional[EmailStr] = None
    created_at: datetime

    class Config:
        from_attributes = True
