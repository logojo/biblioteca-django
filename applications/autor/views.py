from django.shortcuts import render
from django.views.generic import ListView
from .models import Autor

# Create your views here.

class ListAutores(ListView):
    context_object_name = 'autores'
    template_name = "autor/index.html"

    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        #retornando todos los autores desde la funcion creada en el archivo managers donde se crean todas las funciones del modelo
        #return Autor.objects.listarAutores()
        
        #Funcion de busqueda simple por un campos
        #return Autor.objects.buscarAutor(kword)
        
        #Funcion de busqueda por comparando varios campos
        #return Autor.objects.CustomBuscarAutor(kword)
        
        #Funcion de busqueda excluyente
        #return Autor.objects.buscarAutorExclude(kword)    

        #Funcion de busqueda por rango de edad
        return Autor.objects.buscarAutorRangoEdad()
    

