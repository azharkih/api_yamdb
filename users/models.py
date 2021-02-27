from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _

from users.managers import UserManager


class AskRegistration(models.Model):
    """Класс AskRegistration используется для описания модели хранящей
    временные коды регистрации.

    Родительский класс -- models.Model.

    Атрибуты класса
    --------
                                            PK <--
    email : models.EmailField()
        емейл на который отправлен код подтверждения
    confirmation_code : models.TextField()
        сгенерированный код подтверждения
    pub_date : models.DateTimeField()
        дата и время запроса
    """

    email = models.EmailField(
        verbose_name='email',
        help_text='Введите email'
    )
    confirmation_code = models.TextField(
        verbose_name='Код подтвержения',
        help_text='Введите код подтверждения'
    )
    ask_date = models.DateTimeField(
        verbose_name='Дата запроса',
        auto_now_add=True,
        help_text='Укажите дату и время запроса'
    )

    class Meta:
        verbose_name_plural = 'Запросы на регистрацию'
        verbose_name = 'Запрос на регистрацию'
        ordering = ['-ask_date']

    def __str__(self):
        """Вернуть строковое представление в виде email."""
        return self.email


class User(AbstractUser):
    """Класс AskRegistration используется для описания модели хранящей
    временные коды регистрации.

    Родительский класс -- AbstractUser.

    Атрибуты класса
    --------
                                            PK <-- Review, Comment
    bio : models.CharField()
        о пользователе
    email : models.EmailField()
        емейл пользователя
    confirmation_code : models.CharField()
        сгенерированный код подтверждения
    created_at : models.DateTimeField()
        дата и время создания пользователя
    updated_at : models.DateTimeField()
        дата и время создания пользователя
    """

    class Role(models.TextChoices):
        """Класс Role используется для определния допустимых пользовательских
        ролей."""

        USER = 'user', _('Пользователь')
        MODERATOR = 'moderator', _('Модератор')
        ADMIN = 'admin', _('Администратор')

    bio = models.CharField(
        max_length=1000,
        null=True,
        blank=True
    )
    email = models.EmailField(
        db_index=True,
        unique=True
    )
    role = models.CharField(
        max_length=10,
        choices=Role.choices,
        default=Role.USER,
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    class Meta:
        ordering = ('id',)

    def __str__(self):
        """ Строковое представление модели (отображается в консоли) """
        return self.email
