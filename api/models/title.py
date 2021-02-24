from django.db import models

from .category import Category
from .genre import Genre


class Title(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL,
                                 related_name='titles', blank=True, null=True)
    genre = models.ManyToManyField(Genre, related_name='titles', blank=True)
    name = models.CharField(max_length=30)
    year = models.IntegerField(max_length=4)
    description = models.TextField()
