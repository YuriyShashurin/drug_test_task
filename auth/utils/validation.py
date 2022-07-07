from decimal import ROUND_FLOOR
import bcrypt
from app import settings
from sqlalchemy.orm import Session
from auth.models import Profile
from datetime import date
import math
import re


# Валидация возраста
async def valid_user_age(user_birth):
    days_in_year = 365
    user_age = math.floor(int((date.today() - user_birth).days / days_in_year))
    if user_age < 18:
        return False
    else: 
        return True

# Валидация емейла
async def valid_user_email(email):
    check_email = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
    if check_email:
        return True
    else:
        return False

# Валидация номер телефона
async def valid_user_phone(phone):
    print(len(phone))
    if phone.startswith('+7') and len(phone) == 12:
        return True
    else: 
        return False

# Валидация регистрационных данных
async def valid_register_data(auth_data):

    valid_result = {'birth': await valid_user_age(auth_data.birth), 
                    'email': await valid_user_email(auth_data.email), 
                    'phone': await valid_user_phone(auth_data.phone)}
    if all(check == True for check in valid_result.values()):
        valid_result['total_valid_result'] = True
    else:
        valid_result['total_valid_result'] = False
    return valid_result

# Хэширование пароля при регистрации
async def hashed_password(plain_password):
    
    hashed_password = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())
    return hashed_password #возвращаем хэшированный пароль

# Проверка хешированного пароля с паролем из формы для входа в систему
async def check_login_user(login_data, db:Session):
    db_user = db.query(Profile).filter(Profile.login==login_data.login).first()
    if db_user:
        return bcrypt.checkpw(login_data.password.encode(), db_user.password)
    else:
        return None

# Проверка прав на получение данных GET запросов
async def check_authentication(id, db:Session):
    db_user = db.query(Profile).get(id)
    if db_user.is_authenticated:
        return True
    else:
        return False


