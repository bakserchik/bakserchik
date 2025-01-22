from django.contrib import admin

from search.models import Movie



class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'year', 'description') 
    list_filter = ('genre', 'year')  
    search_fields = ('title', 'description')  
    ordering = ('-year',) 
    list_per_page = 20  

class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'genre', 'year', 'description')
    list_editable = ('genre',) 


admin.site.register(Movie, MovieAdmin)


