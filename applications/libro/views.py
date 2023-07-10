from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Libro

from .models import Libro, Categoria

# Create your views here.
 
class ListLibros(ListView):
    template_name = "libro/index.html"
    context_object_name = 'libros'

    def get_queryset(self):
        kword = self.request.GET.get('kword', '')
        fecha1 = self.request.GET.get('fecha1', '')
        fecha2 = self.request.GET.get('fecha2', '')

        if fecha1 and fecha2:
            return Libro.objects.buscarLibroFecha(kword, fecha1, fecha2)
        else:
            #return Libro.objects.buscarLibro(kword)
            return Libro.objects.buscarLibroConTrigram(kword)
        

class ListLibrosCat(ListView):
    template_name = "libro/SearchLibrosCat.html"
    context_object_name = 'libros'

    def get_queryset(self):
        #consulta relacion dos tablas
        return Libro.objects.listarLibrosCategoria(5)
    
        #consulta relacion tres tablas
        #return Categoria.objects.categoriaByAutor(1)

class DetailsLibro(DetailView):
    model = Libro
    template_name = "libro/details.html"
    context_object_name = 'libro'
