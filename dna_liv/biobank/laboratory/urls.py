from django.urls import path
from . import views

""""Отслеживаем переходы на разные ссылки и соответсвенно им выдаем представления"""

urlpatterns = [
    path('', views.list_laboratories, name='list_laboratories'),
    path('create/', views.create_lab, name='create_lab'),
]