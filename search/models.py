
from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(null=True)
    genre = models.CharField(max_length=100, null=True)
    year = models.IntegerField(null=True)
    image = models.ImageField(upload_to='movies/')
    trailer_url = models.URLField(null=True)

    def __str__(self):
        return self.title
