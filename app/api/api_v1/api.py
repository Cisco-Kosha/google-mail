from fastapi import APIRouter

from app.api.api_v1.endpoints import mail

api_router = APIRouter()

api_router.include_router(mail.router, prefix="/mail", tags=["mail"])
