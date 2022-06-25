from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Date, Float
from sqlalchemy.orm import relationship

Base = declarative_base()

class Profile(Base):

    __tablename__ = 'login'
    id = Column(Integer, primary_key=True, index=True, unique=True)
    login = Column(String(50), unique=True)
    password = Column(String(150))
    name = Column(String(30))
    birth = Column(Date)
    phone = Column(String(12))
    tg = Column(String(50), nullable=True)
    email = Column(String(50), nullable=True)
    