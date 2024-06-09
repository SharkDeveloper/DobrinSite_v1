import os

from smtplib import SMTP
from email.message import EmailMessage

EMAIL_LOGIN = os.environ.get('EMAIL_LOGIN')
EMAIL_PASSWORD = os.environ.get('EMAIL_PASSWORD')
SMTP_HOST = os.environ.get('SMTP_HOST')
SMTP_PORT = os.environ.get('SMTP_PORT')


def send_mail(order_id: int, picture_info: str, contacts: str, comment="") -> None:
  msg = EmailMessage()
  msg['Subject'] = f'Заказ №{order_id}'

  msg.set_content(picture_info+"\n\n"+comment+"\n\n"+contacts)

  with SMTP(SMTP_HOST,SMTP_PORT,) as smtp:
    smtp.starttls()
    smtp.ehlo()
    smtp.login(EMAIL_LOGIN, EMAIL_PASSWORD)
    smtp.send_message(msg,EMAIL_LOGIN,EMAIL_LOGIN)
    print('Message sent!')