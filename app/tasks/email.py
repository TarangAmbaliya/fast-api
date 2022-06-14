"""
This module implements email.
"""

from fastapi_mail import MessageSchema
from pydantic import EmailStr

from app.tasks import email


async def welcome_email(to: EmailStr, username: str) -> None:
    """
    This method sends s welcome email to the sender.

    :param to:
        Newly registered user.
    :param username:
        Username to be added in the email body.
    :return None:
    :raises HTTPException:
        When failed to send email and error is looged.
    """

    msg = MessageSchema(
        recipients=[to],
        subject="Welcome Email.!!!",
        template_body={
            "name": username
        }
    )

    await email.send_message(msg, template_name='welcome.html')
    return
