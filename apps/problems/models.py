#  Django
from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=255)


class Problem(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
                                 related_name='problems')
