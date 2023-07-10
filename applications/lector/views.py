from datetime import date
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.views.generic.edit import FormView

from .models import Prestamo
from .forms import FormPrestamos, FormPrestamosMultiple

# Create your views here.

class registrarPrestamo(FormView):
    template_name='lector/create.html'
    form_class = FormPrestamos
    #regresa a la misma vista una vez guardado
    success_url = './create'

    def form_valid(self, form):

        #para usar el ORM siempre se usa el metodo objects
        # Prestamo.objects.create(
        #     lector = form.cleaned_data['lector'],
        #     libro = form.cleaned_data['libro'],
        #     fecha_prestamo = date.today(),
        #     devuelto = False
        # )

        #de esta form se puede crear y actualizar
        prestamo = Prestamo(
            lector = form.cleaned_data['lector'],
            libro = form.cleaned_data['libro'],
            fecha_prestamo = date.today(),
            devuelto = False
        )

        #actualizando otra tabla desdepues de crear un registro en otra
        libro = form.cleaned_data['libro']
        libro.stock =  libro.stock - 1
        libro.visitas =  libro.visitas + 1
        libro.save()

        prestamo.save()
        return super(registrarPrestamo, self).form_valid(form)



class registrarPrestamo2(FormView):
    template_name='lector/create.html'
    form_class = FormPrestamos
    success_url = './create'

    def form_valid(self, form):
        
        #validando si registro exise
        #si existe lo recupera y si no lo crea
        #En obj se almacena el registro recuperado o creado
        #La variable created regresa un booleano si se creo regresa "true" si no un "false"
        #existe un update_or_create
        obj, created = Prestamo.objects.get_or_create(
            #get
            lector = form.cleaned_data['lector'],
            libro =  form.cleaned_data['libro'],
            devuelto = False,
            #create
           defaults={
             'fecha_prestamo': date.today()
           }
        )

        if created:
            return super(registrarPrestamo2, self).form_valid(form)
        else:
            return HttpResponseRedirect('/')
        

        
class registrarPrestamoMultiple(FormView):
    template_name='lector/multiple.html'
    form_class = FormPrestamosMultiple
    #regresa a la misma vista una vez guardado
    success_url = './multiple'

    def form_valid(self, form):
        #extrayendo datos enviados desde el formulario e imprimiendolos
        print(form.cleaned_data['libros'])

        prestamos = []
        for book in form.cleaned_data['libros']:
           prestamo = Prestamo(
                lector = form.cleaned_data['lector'],
                libro = book,
                fecha_prestamo = date.today(),
                devuelto = False
            )
           
           #agregando elementos al array
           prestamos.append(prestamo)

        #guardando array en bd
        #existe un bulk_update
        Prestamo.objects.bulk_create(prestamos)


        return super(registrarPrestamoMultiple, self).form_valid(form)