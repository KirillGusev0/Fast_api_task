# -*- coding: utf-8 -*-

from pydantic import Field, BaseModel, ConfigDict, EmailStr
from typing import Optional
from itertools import count
from pydantic.dataclasses import dataclass
from dataclasses import field

_id_counter_user = count(1)


def id_gen_user():
    return next(_id_counter_user)



class User(BaseModel):
    
        
    model_config = ConfigDict(
       title="User",
       description = "User model",
       populate_by_name=True
    )
    
   
           
    
    id: int = Field(default_factory = id_gen_user, gt=0)
    name: str = Field(min_length=1)
    username: str = Field( min_length=1)
    password: str = Field(min_length=1)
    email: Optional[EmailStr] = None
    
@dataclass
class UserStorage:
    _instance = None
    _users: list[User] = field(default_factory=list)

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super().__new__(cls)
            cls._instance._users = []
        return cls._instance

    def add(self, new_data: User):
        self._users.append(new_data)

    def get_all(self):
        return self._users
    
    


