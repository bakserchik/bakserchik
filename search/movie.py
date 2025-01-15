from django.db import models

class Movie(models.Model):
    title = models.CharField(max_length=200)   
    image = models.ImageField(upload_to='movie_image/')  


    def __str__(self):
        return self.title
    
    
