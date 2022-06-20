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
logger = logging.getLogger("budget_bot_log")

from auth import views
# Add router
app.include_router(views.auth_router, prefix='/v1', tags=["rest"])

from starlette.requests import Request
from starlette.responses import Response
from .db import SessionLocal




@app.middleware('http')
async def db_session_middleware(request: Request, call_next):
    response = Response('Internet server error', status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response