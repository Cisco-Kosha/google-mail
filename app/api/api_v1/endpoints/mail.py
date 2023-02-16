from typing import Any, List, Optional

from fastapi import APIRouter, Depends, HTTPException, UploadFile, FastAPI, File
from googleapiclient import discovery
from starlette.responses import JSONResponse

from app.crud import crud_mail
from app.crud.crud_mail import get_credentials, CreateMessage, SendMessageInternal
from app.schemas.mail import SendEmail

from app.utils import exception

from oauth2client import file
import oauth2client
from oauth2client import client, tools

router = APIRouter()


@router.post("/", response_model=List[Any])
def send_email(send_email: SendEmail) -> Any:
    credentials = get_credentials()
    # credentials = get_credentials()
    # http = credentials.authorize(httplib2.Http())
    service = discovery.build('gmail', 'v1', credentials=credentials)
    message1 = CreateMessage(send_email.from_email, send_email.to_email, send_email.email_subject, send_email.email_body)
    res = SendMessageInternal(service, "me", message1)
    return JSONResponse(res)

