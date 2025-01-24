"""
URL configuration for name project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf import settings
from django.conf.urls.static import static
from django.urls import path


from django.urls import path
from search import views

urlpatterns = [
    path('', views.home, name='home'),
    path('search/', views.search, name='search'),
    path('admin/search/', views.admin_search, name='admin_search'),
    path('add/', views.add_movie, name='add_movie'),
    path('movie_list/', views.movie_list, name='movie_list'),  
    path('add_to_cart/<int:movie_id>/', views.add_to_cart, name='add_to_cart'),
    path('view_cart/', views.view_cart, name='view_cart'),
    path('favorite/<int:pk>/', views.toggle_favorite, name='toggle_favorite'),
    path('favorites/', views.favorite_list, name='favorite_list'),
    path('', views.home, name='home'),
    path('toggle_favorite/<int:movie_id>/', views.toggle_favorite, name='toggle_favorite'),
    path('view_cart/', views.view_cart, name='view_cart'),  

]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


