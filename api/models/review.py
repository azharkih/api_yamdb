from django.db import models

from .user import User
from .title import Title


class Review(models.Model):
    author = models.ForeignKey(User, 
        on_delete=models.CASCADE, blank=True, null=True, related_name="reviews")
    title = models.ForeignKey(Title, 
        on_delete=models.CASCADE, related_name="reviews", blank=True, null=True)
    score = models.IntegerField(null=True)
    text = models.TextField()
    pub_date = models.DateTimeField("Дата добавления", 
        auto_now_add=True, db_index=True)

    def __str__(self) -> str:
        return f'{self.author.username} - {self.text}'
