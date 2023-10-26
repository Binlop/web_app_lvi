from django.urls import path
from . import views

""""Отслеживаем переходы на разные ссылки и соответсвенно им выдаем представления"""

urlpatterns = [
    path('', views.biobank_home, name='biobank_home'),
    path('biospecimen/', views.biospecimen, name='biospecimen'), 
    path('create/', views.create_biospecimen, name='create_biospecimen'),
]