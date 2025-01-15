
from django.contrib import admin
from .models import Movie

class MovieAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'image')  
    search_fields = ('title',) 

admin.site.register(Movie, MovieAdmin)


