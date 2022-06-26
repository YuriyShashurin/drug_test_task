from sqlalchemy.orm import Session
from app import logger

from auth.models import Profile

async def add_new_user(auth_data, db:Session):
    try:
        new_user = Profile(**auth_data.dict())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        logger.info(f'The User {new_user.id} added')
        return new_user
    except Exception as e:
        return e

async def login_user(login_data, db):
    user = db.query(Profile).filter(Profile.login==login_data.login).first()
    user.is_authenticated = True
    db.commit()
    db.refresh(user)
    logger.info(f'The User @{login_data.login} logged in')
    return user


async def logout_user(id: int, db: Session):
    user = db.query(Profile).get(id.id)
    user.is_authenticated = False
    db.commit()
    db.refresh(user)
    logger.info(f'The User {id} logged out')


# получение данных о пользователи по айди
async def get_user_by_id(id: int, db: Session):

    db_user = db.query(Profile).get(id)

    return db_user



