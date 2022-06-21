from pydantic import BaseModel,EmailStr
from datetime import date
from typing import Optional


class UserBase(BaseModel):
    login: str
    password : str
    name: str
    birth: date
    phone: str
    tg: Optional[str]
    email : Optional[EmailStr]
    


class UserCreate(UserBase):
    pass


class User(UserBase):
    id: int


    class Config:
        orm_mode = True