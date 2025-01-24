from django.db import models
from django.contrib.auth.models import User

class Movie(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='movies/')
    description = models.TextField()
    genre = models.CharField(max_length=100)  # Поле genre
    year = models.IntegerField()  # Поле year
    trailer_url = models.URLField()
    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    favorite_movies = models.ManyToManyField(Movie, related_name='favorite_by_users', blank=True)

    def __str__(self):
        return f"Profile of {self.user.username}"
