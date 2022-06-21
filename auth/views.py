from fastapi import APIRouter, Depends, HTTPException
from app.db import SessionLocal
from sqlalchemy.orm import Session
from auth import schemas
from auth.utils import crud


auth_router = APIRouter()

def get_postgres_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@auth_router.post('/auth/create_user/', response_model=schemas.User,status_code=201)
async def create_user(auth_data: schemas.UserCreate, db: Session = Depends(get_postgres_db)):
    try:
        await crud.add_new_user(auth_data, db)
    except Exception as e:
        raise HTTPException(status_code=e.code,detail=e.message)

