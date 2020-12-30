from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.bbb, name = 'login_url'),
]