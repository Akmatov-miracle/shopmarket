from django.dispatch import receiver
from django.urls import reverse
from django_rest_passwordreset.signals import reset_password_token_created
from django.core.mail import send_mail


def send_confirmation_email(user):
    code = user.activation_code  # берем у юзера активационный код
    full_link = f'http://localhost:8000/api/v1/accounts/activate/{code}'  # ссылка которая придет юзеру на поту
    to_email = user.email  # берем у юзера его емаил
    send_mail(
        'Subject here',
        full_link,
        'from@example.com',
        [to_email],
        fail_silently=False,
    )

@receiver(reset_password_token_created)
def password_reset_token_created(sender, instance, reset_password_token, *args, **kwargs):
    email_plaintext_message = "{}?token={}".format(reverse('password_reset:reset-password-request'), reset_password_token.key)
    send_mail(
        # title:
        "Password Reset for {title}".format(title="Etno shopmarket"),
        # message:
        email_plaintext_message,
        # from:
        "aidanekbekmamatova@gmail.com",
        # to:
        [reset_password_token.user.email]
    )