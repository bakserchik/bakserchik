from django.urls import path
from . import views

urlpatterns = [
    path('search/', views.search, name='search'),
    path('admin/search/', views.admin_search, name='admin_search'),  
]
