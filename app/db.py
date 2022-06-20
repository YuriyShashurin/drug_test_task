from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app import settings


SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://{postgres_name}:{postgres_password}@{postgres_host}/{postgres_db}'.format(
    postgres_name=settings.postgres_name,
    postgres_password=settings.postgres_password,
    postgres_host=settings.postgres_host,
    postgres_db=settings.postgres_db
)


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)