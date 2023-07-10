from django.contrib import admin
from django.urls import path

from . import views 

urlpatterns = [
    path('prestamos/create', views.registrarPrestamo2.as_view(), name='prestamos'),
    path('prestamos/multiple', views.registrarPrestamoMultiple.as_view(), name='multi-prestamos'),
]
