# В вашем приложении urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('', views.processing_dna, name='dna-length'),
    path('add/', views.dna_length_add, name='dna-length-add'),
    path('add-properties/', views.dna_analysis, name='dna_analysis'),
]
