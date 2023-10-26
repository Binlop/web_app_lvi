from django.urls import path
from . import views

urlpatterns = [
    path('', views.biobank_home, name='biobank_home'), #Отслеживаем переход на директорию news
    path('biospecimen/', views.biospecimen, name='biospecimen'), #Отслеживаем переход на директорию news
    path('create/', views.create_biospecimen, name='create_biospecimen'), #Отслеживаем переход на директорию create
]