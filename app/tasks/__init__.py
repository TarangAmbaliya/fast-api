"""
Converting to Module.
"""

from pydantic import EmailStr
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from pathlib import Path

conf = ConnectionConfig(
    MAIL_USERNAME='b982e751d200d2',
    MAIL_PASSWORD='fac0e013df5431',
    MAIL_FROM=EmailStr('fastapi@mail.com'),
    MAIL_PORT=2525,
    MAIL_SERVER='smtp.mailtrap.io',
    MAIL_TLS=True,
    MAIL_SSL=False,
    TEMPLATE_FOLDER=Path(__file__).parent/'templates'
)

email = FastMail(config=conf)
