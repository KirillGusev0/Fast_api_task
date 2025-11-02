# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class UserCreate(BaseModel):
    name: str = Field(min_length=1)
    username: str = Field(min_length=1)
    password: str = Field(min_length=1)
    email: Optional[EmailStr] = None


class UserRead(BaseModel):
    id: int
    name: str
    username: str
    email: Optional[EmailStr] = None

    class Config:
        from_attributes = True
    