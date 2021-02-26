from django.db import models

from .user import User
from .review import Review


class Comment(models.Model):
    author = models.ForeignKey(User, 
        on_delete=models.CASCADE, blank=True, null=True, related_name="comments")
    review = models.ForeignKey(Review, 
        on_delete=models.CASCADE, related_name="comments", blank=True, null=True)
    text = models.TextField()
    pub_date = models.DateTimeField("Дата добавления", 
        auto_now_add=True, db_index=True)

    def __str__(self) -> str:
        return f'{self.author.username} - {self.text}'
