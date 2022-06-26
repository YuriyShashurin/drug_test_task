from fastapi import APIRouter, Depends, HTTPException
from app.db import SessionLocal
from app import logger
from sqlalchemy.orm import Session
from auth import schemas, my_exceptions
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



# Обработка запроса на регистрацию пользователя
@auth_router.post('/auth/register/', response_model=schemas.UserResponse,status_code=201)
async def create_user(auth_data: schemas.UserCreate, db: Session = Depends(get_postgres_db)):
    valid_form = await validation.valid_register_data(auth_data)
    if valid_form['total_valid_result']:
        try:
            hashed_password = await validation.hashed_password(auth_data.password)
            auth_data.password = hashed_password.decode()
            new_user = await crud.add_new_user(auth_data, db)
            try:
                if new_user.id:
                    return new_user
            except:
                raise new_user

        except Exception as e:
            logger.error(e)
            detail = {
                'status':500,
                'message': e.orig.args[0]
            }
            raise HTTPException(status_code=500, detail=detail)

    else:
        messages = []

        del valid_form['total_valid_result']
        for key, value in valid_form.items():
            if value==False:
                messages.append(f'Поле {key} не прошло валидацию')

        detail = {
            'status':422,
            'message': messages
        }
        raise HTTPException(status_code=500,
                            detail=detail,
                            headers={"Content-Type": "application/json"},)


# Обработка входа пользователя с логином и паролем
@auth_router.post('/auth/login/', response_model=schemas.UserResponse,status_code=201)
async def login_user(login_data: schemas.LoginUserBase, db: Session = Depends(get_postgres_db)):
    check_login_data = await validation.check_login_user(login_data, db) #Проверка логина и пароля
    if check_login_data: #Обработка, если логин и пароль совпадают с БД
        db_user = await crud.login_user(login_data, db) #Аутентификация пользователя
        return db_user
    else:  #Обработка неправильного ввода, в целом по связке логин/пароль, чтобы не давать подсказски пользователям)
        detail = {
            'status':404,
            'message': 'Введены неверные логин/пароль',
        }
        raise HTTPException(status_code=404, detail=detail)


# Обработка запроса на выход
@auth_router.post('/auth/logout/', status_code=201)
async def logout_user(id: schemas.User, db: Session = Depends(get_postgres_db)):
    await crud.logout_user(id, db)


# Обработка запрос на получение данных о пользователи по айди
@auth_router.get('/user/', response_model=schemas.UserItem,status_code=200)
async def get_user(id: int, db: Session = Depends(get_postgres_db)):
    try:
        user = await crud.get_user_by_id(id, db)
        if user == None:
            raise my_exceptions.UserNotFoundError(id)
        else:
            return user

    except Exception as e:
        e.get_error_text()
        detail = {
            'status':e.__dict__['status'],
            'message': e.__dict__['text'],
        }
        raise HTTPException(status_code=404, detail=detail)
