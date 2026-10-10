from django.db import models


class Book(models.Model):
    
    title = models.CharField(
        max_length=200,
    ) 
    author = models.CharField(
        max_length=150,
    )
    isbn = models.CharField(
        max_length=13,
        unique=True,
    )
    volume = models.PositiveIntegerField(
        blank=True,
        null=True,
    )
    description = models.TextField(
        max_length=1000,
        blank=False,
    )
    publication_year = models.PositiveIntegerField(
        null=True,
        blank=True,
    )