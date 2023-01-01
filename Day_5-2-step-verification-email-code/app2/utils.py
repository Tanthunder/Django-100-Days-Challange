
from django.core.mail import send_mail
from django.conf import settings

def email( code, mail ):
    "Send email with verification code."
    subject = 'Hello'
    message = f'Your verification code is {code}'
    send_mail(
        subject,
        message,
        settings.EMAIL_HOST_USER,
        [mail],
        fail_silently= False
    )