from django.urls import path
from . import views

urlpatterns = [
    # Главная страница будет доступна по корню сайта (http://127.0.0.1:8000/)
    path('', views.home, name='home'),

    # Страница контактов будет доступна по адресу /contacts/
    path('contacts/', views.contacts, name='contacts'),
]
