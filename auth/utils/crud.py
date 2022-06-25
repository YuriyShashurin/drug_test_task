from sqlalchemy.orm import Session
from app import logger

from auth.models import Profile

async def add_new_user(auth_data, db:Session):
    try:
        new_user = Profile(**auth_data.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        logger.info(f'User {new_user.id} added')
        return new_user
    except Exception as e:
        return e



