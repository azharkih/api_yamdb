import uuid

from django.core.mail import send_mail

from api_yamdb import settings
from users.models import AskRegistration


def send_confirmation_code(email, confirmation_code):
    """ Отправить код подтверждения на емейл."""

    header = 'Код подтверждения регистрации'
    text = ('Ранее вы отправляли запрос на регистрацию в yamdb. Ваш код '
            f'подтверждения: {confirmation_code}')
    email_from = settings.EMAIL_FROM
    send_mail(header, text, email_from, [email, ])


def save_ask_registration(email, confirmation_code):
    """ Сохранить сгенерированный код в базу."""

    values = {'email': email, 'confirmation_code': confirmation_code}
    AskRegistration.objects.update_or_create(email=email, defaults=values)


def registration(email):
    """ Выполнить обработку запроса на регистрацию."""

    confirmation_code = str(uuid.uuid4())
    send_confirmation_code(email, confirmation_code)
    save_ask_registration(email, confirmation_code)
