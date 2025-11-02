# -*- coding: utf-8 -*-
from pydantic import BaseModel, Field, EmailStr
from typing import Optional

class RegisterUser(BaseModel):
    
    
    name: str = Field(min_length=1)
    username: str = Field(min_length=1)
    password: str = Field(min_length=1)
    email: Optional[EmailStr] = None
    
    
class LoginUser(BaseModel):
    username: str = Field(min_length=1)
    password: str = Field(min_length=1)

class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"