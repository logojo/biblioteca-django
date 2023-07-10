from django.contrib import admin
from django.urls import path

from . import views 

urlpatterns = [
    path('libros/', views.ListLibros.as_view(), name='libros'),
    path('libros-2/', views.ListLibrosCat.as_view(), name='libros-2'),
    path('libro-details/<pk>', views.DetailsLibro.as_view(), name='detalles'),
]
