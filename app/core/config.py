import os
import secrets
from typing import Any, Dict, List, Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, HttpUrl, validator
from logging.config import dictConfig
import logging
from app.utils.logging import LogConfig

class Settings(BaseSettings):
    API_V1_STR: str = "/api/v1"
    SECRET_KEY: str = secrets.token_urlsafe(32)
    PROJECT_NAME: str = "google-mail"
    # 60 minutes * 24 hours * 8 days = 8 days
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 60 * 24 * 8

    # BACKEND_CORS_ORIGINS is a JSON-formatted list of origins
    # e.g: '["http://localhost", "http://localhost:4200", "http://localhost:3000", \
    # "http://localhost:8080", "http://local.dockertoolbox.tiangolo.com"]'
    BACKEND_CORS_ORIGINS: List[AnyHttpUrl] = []
    ACCESS_TOKEN: str = os.getenv('ACCESS_TOKEN', '')
    REFRESH_TOKEN: str = os.getenv('REFRESH_TOKEN', '')
    EXPIRES_AT: str = os.getenv('EXPIRES_AT', '')
    CLIENT_ID: str = os.getenv('CLIENT_ID', '')
    CLIENT_SECRET: str = os.getenv('CLIENT_SECRET', '')

    @validator("BACKEND_CORS_ORIGINS", pre=True)
    def assemble_cors_origins(cls, v: Union[str, List[str]]) -> Union[List[str], str]:
        if isinstance(v, str) and not v.startswith("["):
            return [i.strip() for i in v.split(",")]
        elif isinstance(v, (list, str)):
            return v
        raise ValueError(v)

settings = Settings()

dictConfig(LogConfig().dict())
logger = logging.getLogger(settings.PROJECT_NAME)