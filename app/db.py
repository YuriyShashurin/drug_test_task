from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app import settings,logger
import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT



def create_db(db_name):
    print(settings.postgres_password)
    conn = psycopg2.connect(user=settings.postgres_name, password=settings.postgres_password, host=settings.postgres_host)
    conn.set_session(autocommit=True)
    conn.set_isolation_level(
        ISOLATION_LEVEL_AUTOCOMMIT
    )
    with conn.cursor() as cur:
        try:
            cur.execute("CREATE DATABASE " + db_name) # создание бд с названием БД из сеттинга
            logger.info(f"DB '{db_name}' has been added")
        except psycopg2.errors.DuplicateDatabase as e:
            logger.info(f"DB '{db_name}' already exists")

    conn.close()


def create_tables(db_name):
    conn = psycopg2.connect(dbname=settings.postgres_db,user=settings.postgres_name, password=settings.postgres_password, host=settings.postgres_host)
    with conn.cursor() as cur:
        try:
            with open('create_tables.sql') as f:
                cur.execute(f.read()) # Добавление таблиц
                logger.info("Tables have been added")
        except psycopg2.ProgrammingError as e:
            logger.info("Tables already exists")

    conn.commit()
    conn.close()


SQLALCHEMY_DATABASE_URL = 'postgresql+psycopg2://{postgres_name}:{postgres_password}@{postgres_host}/{postgres_db}'.format(
    postgres_name=settings.postgres_name,
    postgres_password=settings.postgres_password,
    postgres_host=settings.postgres_host,
    postgres_db=settings.postgres_db
)


engine = create_engine(SQLALCHEMY_DATABASE_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)