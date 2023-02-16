import base64
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from typing import List, Any

import oauth2client
from google.oauth2.credentials import Credentials
from googleapiclient import errors
import os

from oauth2client import client, tools

from app.utils import exception
import json
from app.core.config import settings, logger

auth_uri = "https://accounts.google.com/o/oauth2/auth"
token_uri = "https://oauth2.googleapis.com/token"
SCOPES = 'https://www.googleapis.com/auth/gmail.send https://www.googleapis.com/auth/gmail.readonly'


def get_credentials():
    '''
    cr = {"installed": {"client_id": "1070447801305-e1cn32a6gus7u9dcvutkhhh0frcr4m73.apps.googleusercontent.com",
                        "project_id": "kosha-377913", "auth_uri": "https://accounts.google.com/o/oauth2/auth",
                        "token_uri": "https://oauth2.googleapis.com/token",
                        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                        "client_secret": "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", "redirect_uris": ["http://localhost"]}}
    '''

    cr = {"installed": {"client_id": settings.CLIENT_ID,
                        "project_id": "kosha-377913", "auth_uri": auth_uri,
         "token_uri": token_uri,
                        "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
                        "client_secret": settings.CLIENT_SECRET, "redirect_uris": ["http://localhost"]}}
    with open('credentials.json', 'w') as f:
        json.dump(cr, f)
    try:
        home_dir = os.path.expanduser('~')
        credential_dir = os.path.join('', '.credentials')
        if not os.path.exists(credential_dir):
            os.makedirs(credential_dir)
        credential_path = os.path.join(credential_dir, 'file1.json')
        store = oauth2client.file.Storage(credential_path)
        credentials = store.get()
        if not credentials or credentials.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            flow.user_agent = "Kosha"
            flags = oauth2client.tools.argparser.parse_args(args=[])
            credentials = tools.run_flow(flow, store, flags)
    except Exception as e:
        print(e)
    return credentials



def CreateMessage(sender, to, subject, msgHtml):
    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = to
    msg.attach(MIMEText(msgHtml, 'html'))
    raw = base64.urlsafe_b64encode(msg.as_bytes())
    raw = raw.decode()
    body = {'raw': raw}
    return body


def SendMessageInternal(service, user_id, message):
    try:
        message = (service.users().messages().send(userId=user_id, body=message).execute())
        print('Message Id: %s' % message['id'])
        return message
    except errors.HttpError as error:
        print('An error occurred: %s' % error)
