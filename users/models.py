from django.contrib.auth.models import (
    AbstractBaseUser, BaseUserManager, PermissionsMixin
)
from django.db import models
from django.utils.translation import gettext_lazy as _


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


class UserManager(BaseUserManager):
    """Класс UserManager используется для описания менеджера модели User.
    """

    def create_user(self, username, email, password=None):
        """ Создает и возвращает пользователя с емейлом, паролем и именем. """
        if username is None:
            raise TypeError('Users must have a username.')

        if email is None:
            raise TypeError('Users must have an email address.')

        user = self.model(username=username, email=self.normalize_email(email))
        user.set_password(password)
        user.save()

        return user

    def create_superuser(self, username, email, password):
        """ Создает и возввращет пользователя с привилегиями суперадмина. """
        if password is None:
            raise TypeError('Superusers must have a password.')

        user = self.create_user(username, email, password)
        user.is_superuser = True
        user.save()

        return user


class User(AbstractBaseUser, PermissionsMixin):
    """Класс AskRegistration используется для описания модели хранящей
    временные коды регистрации.

    Родительский класс -- AbstractBaseUser, PermissionsMixin.

    Атрибуты класса
    --------
                                            PK <-- Review, Comment

    first_name : models.CharField()
        имя пользователя
    last_name : models.CharField()
        фамилия пользователя
    username : models.CharField()
        юзернейм пользователя
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

    first_name = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    last_name = models.CharField(
        max_length=200,
        null=True,
        blank=True
    )
    username = models.CharField(
        db_index=True,
        max_length=255,
        unique=True
    )
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
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    updated_at = models.DateTimeField(
        auto_now=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    objects = UserManager()

    def __str__(self):
        """ Строковое представление модели (отображается в консоли) """
        return self.email
