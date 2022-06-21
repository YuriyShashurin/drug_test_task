from fastapi import FastAPI
from .config import Config_settings
from logging.config import dictConfig
import logging
from .logs_config import LogConfig


# initial settings
settings = Config_settings()


# initial app
app = FastAPI()

# initial logger
dictConfig(LogConfig().dict())
logger = logging.getLogger("drug_test_task")

from auth import views
# Add router
app.include_router(views.auth_router, prefix='/v1', tags=["rest"])

from starlette.requests import Request
from starlette.responses import Response
from .db import SessionLocal, create_db, create_tables

create_db(settings.postgres_db) # создание бд с названием БД из сеттинга, если она не существует
create_tables(settings.postgres_db) # создание схемы таблицы, если она не существует


@app.middleware('http')
async def db_session_middleware(request: Request, call_next):
    response = Response('Internet server error', status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

