from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, Integer, ForeignKey, Date, Float, Boolean, LargeBinary
from sqlalchemy.orm import relationship
from sqlalchemy.dialects.postgresql import UUID
import uuid

Base = declarative_base()

class Profile(Base):

    __tablename__ = 'profile'
    id = Column(UUID(as_uuid=True), primary_key=True, index=True, unique=True,default=uuid.uuid4)
    login = Column(String(50), unique=True)
    password = Column(LargeBinary)
    name = Column(String(30))
    birth = Column(Date)
    phone = Column(String(12))
    tg = Column(String(50), nullable=True)
    email = Column(String(50), nullable=True)
    is_authenticated = Column(Boolean, default=False)
    