from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_article, name = 'add_article'),
    path('update/', views.add_article, name = 'update_article'),
    path('delete/', views.add_article, name = 'delete_article'),
] 


