from decimal import ROUND_FLOOR
import bcrypt
from app import settings
from sqlalchemy.orm import Session
from auth.models import Profile
from datetime import date
import math
import re



async def valid_user_age(user_birth):
    days_in_year = 365
    user_age = math.floor(int((date.today() - user_birth).days / days_in_year))
    if user_age < 18:
        return False
    else: 
        return True


async def valid_user_email(email):
    check_email = re.search(r'[\w.-]+@[\w.-]+.\w+', email)
    if check_email:
        return True
    else:
        return False


async def valid_user_phone(phone):
    pass


async def valid_register_data(auth_data):
    check_age = await valid_user_age(auth_data.birth)
    check_email = await valid_user_email(auth_data.email)
    check_phone = await valid_user_phone(auth_data.phone)
    if check_email and check_age and check_phone:
        return True
    else:
        return False


async def hashed_password(plain_password):
    
    hashed_password = bcrypt.hashpw(plain_password.encode(), bcrypt.gensalt())
    return hashed_password #возвращаем хэшированный пароль


async def check_login_user(login_data, db:Session):
    db_user = db.query(Profile).filter(Profile.login==login_data.login).first()
    if db_user:
        return bcrypt.checkpw(login_data.password.encode(), db_user.password.encode())
    else:
        return None


