from datetime import datetime as dt

from django.core.exceptions import ValidationError


def score_validator(value):
    if value <= 0 or value > 10:
        raise ValidationError('Рейтинг может быть в диапозоне от 1 до 10')


def year_validator(value):
    current_year = dt.now().year
    if value > current_year:
        raise ValidationError(
            'Год произведения не может быть больше текущего'
        )
