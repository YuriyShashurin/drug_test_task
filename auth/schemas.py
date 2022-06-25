from pydantic import BaseModel,EmailStr
from datetime import date
from typing import Optional


class UserBase(BaseModel):
    login: str
    password : str

    


class UserCreate(UserBase):
    name: str
    birth: date
    phone: str
    tg: Optional[str]
    email : Optional[EmailStr]


class User(BaseModel):
    id: int


    class Config:
        orm_mode = True


