from pydantic import BaseModel,EmailStr,UUID4
from datetime import date
from typing import Optional

# Модель для принятия данных для логина
class LoginUserBase(BaseModel):
    login: str
    password : str

    

# Модель для принятия данных для логина
class UserCreate(LoginUserBase):
    name: str
    birth: date
    phone: str
    tg: Optional[str]
    email : Optional[EmailStr]



class User(BaseModel):
    id: UUID4


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
