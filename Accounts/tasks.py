from celery import shared_task
from django.core.mail import send_mail

from Accounts.send_mail import send_confirmation_email


@shared_task
def send_confirmation_email_task(code, email):
    send_confirmation_email(code, email)


