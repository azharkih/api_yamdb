from django.db import models


class AskRegistration(models.Model):
    """Класс AskRegistration используется для описания модели хранящей
    временные коды регистрации.

    Родительский класс -- models.Model.

    Атрибуты класса
    --------
                                            PK <--
    email : models.TextField()
        текст сообщения
    confirmation_code : models.TextField()
        сгенерированный код подтверждения
    pub_date : models.DateTimeField()
        дата и время запроса

    Методы класса
    --------

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
