from pydantic import BaseModel,EmailStr
from datetime import date
from typing import Optional


class LoginUserBase(BaseModel):
    login: str
    password : str

    


class UserCreate(LoginUserBase):
    name: str
    birth: date
    phone: str
    tg: Optional[str]
    email : Optional[EmailStr]



class User(BaseModel):
    id: int


class UserResponse(User):
    is_authenticated: bool


    class Config:
        orm_mode = True


class UserItem(UserResponse):
    login: str
    name: str
    birth: date
    phone: str
    tg: Optional[str]
    email : Optional[EmailStr]

    class Config:
        orm_mode = True
