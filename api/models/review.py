from django.db import models

from .user import User
from .title import Title


class Review(models.Model):
    author = models.ForeignKey(User, 
        on_delete=models.CASCADE, related_name="reviews")
    title = models.ForeignKey(Title, 
        on_delete=models.CASCADE, related_name="reviews")
    text = models.TextField()
    created = models.DateTimeField("Дата добавления", 
        auto_now_add=True, db_index=True)

    def __str__(self) -> str:
        return f'{self.author.username} - {self.text}'
