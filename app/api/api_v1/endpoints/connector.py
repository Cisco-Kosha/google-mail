from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException

from fastapi.responses import JSONResponse

from fastapi import Request

router = APIRouter()


@router.get("/list", response_model=Any)
def get_connector_spec():
    return JSONResponse({"ACCESS_TOKEN": "OAuth2 Access Token", "REFRESH_TOKEN": "OAuth2 Refresh Token", "EXPIRES_AT": "OAuth2 Expires At",
                         "CLIENT_ID":"OAuth2 Client ID", "CLIENT_SECRET": "OAuth2 Client Secret"})


@router.post("/test", response_model=Any)
async def check_connector_spec(request: Request):
    data = await request.json()
    if data is not None:
        return True
    else:
        return False
