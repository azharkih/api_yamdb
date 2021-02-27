from django.contrib.auth.base_user import BaseUserManager


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
