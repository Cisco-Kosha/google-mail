from typing import Optional

from pydantic import BaseModel, Extra


class SendEmail(BaseModel):
    email_subject: str
    from_email: str
    to_email: str
    email_body: str
