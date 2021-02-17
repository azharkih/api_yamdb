import random
import string

from django.core.mail import send_mail

from api_yamdb import settings
from users.models import AskRegistration


def generate_confirmation_code():
    chars = string.punctuation + string.ascii_letters + string.digits
    confirmation_code = ''.join(random.choice(chars) for _ in range(10))
    return confirmation_code


def send_confirmation_code(email, confirmation_code):
    header = 'Код подтверждения регистрации'
    text = ('Ранее вы отправляли запрос на регистрацию в yamdb. Ваш код '
            f'подтверждения: {confirmation_code}')
    email_from = settings.EMAIL_FROM
    send_mail(header, text, email_from, [email, ]
              # fail_silently=False
              )


def save_ask_registration(email, confirmation_code):
    values = {'email': email, 'confirmation_code': confirmation_code}
    AskRegistration.objects.update_or_create(email=email, defaults=values)


def registration(email):
    confirmation_code = generate_confirmation_code()
    send_confirmation_code(email, confirmation_code)
    save_ask_registration(email, confirmation_code)
