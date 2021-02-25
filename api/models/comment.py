from django.db import models

from .user import User
from .review import Review


class Comment(models.Model):
    author = models.ForeignKey(User, 
        on_delete=models.CASCADE, related_name="comments")
    review = models.ForeignKey(Review, 
        on_delete=models.CASCADE, related_name="comments")
    text = models.TextField()
    created = models.DateTimeField("Дата добавления", 
        auto_now_add=True, db_index=True)

    def __str__(self) -> str:
        return f'{self.author.username} - {self.text}'
