from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'), 
    path('search/', views.search, name='search'),
    path('admin/search/', views.admin_search, name='admin_search'),
]
