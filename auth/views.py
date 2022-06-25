from fastapi import APIRouter, Depends, HTTPException
from app.db import SessionLocal
from app import logger
from sqlalchemy.orm import Session
from auth import schemas
from auth.utils import crud, validation
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse


auth_router = APIRouter()

def get_postgres_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()




@auth_router.post('/auth/register/', response_model=schemas.User,status_code=201)
async def create_user(auth_data: schemas.UserCreate, db: Session = Depends(get_postgres_db)):
    valid_form = await validation.valid_register_data(auth_data)
    if valid_form:
        try:
            plain_password = auth_data.password
            hashed_password = await validation.hashed_password(plain_password)
            auth_data.password = hashed_password.decode()
            new_user = await crud.add_new_user(auth_data, db)
            try:
                if new_user.id:
                    return new_user
            except:
                raise new_user

        except Exception as e:
            logger.error(e)
            raise HTTPException(status_code=500, detail=e.orig.args)

    else:
        print('не свалидирован')

@auth_router.post('/auth/login/', response_model=schemas.User,status_code=201)
async def login_user(login_data: schemas.UserBase, db: Session = Depends(get_postgres_db)):
    check_login_data = await validation.check_login_user(login_data, db)
    print(check_login_data)

