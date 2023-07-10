
from django import forms
from .models import Prestamo
from applications.libro.models import Libro

class FormPrestamos(forms.ModelForm):
    
    #con los metadatos estoy conectando a la modelo prestamo y convetir cada campo en parte  de un formulario html
    class Meta:
        model = Prestamo
        fields = (
            'lector',
            'libro',
        )

class FormPrestamosMultiple(forms.ModelForm):

    #Ya que la relacion entre libros y prestamos no es de muchos a muchos
    #Se crear este tipo de formulario para poder agregar varios libros a un lector  sin realizar varias consultas
    #Se esta extrayendo un conjunto de datos del modelo libro
    libros = forms.ModelMultipleChoiceField(
        #Carga todos los campos del modelo libros
        #queryset = Libro.objects.all() 

        queryset = None,
        required=True,
        widget=forms.CheckboxSelectMultiple, 
    )

    class Meta:
        model = Prestamo
        fields = (
            'lector',
        )

    #la funcion init Inicializa un formulario si se quiere que se muestre con un valor predeterminado dentro del Html
    def __init__(self, *args, **kwards):
        super(FormPrestamosMultiple, self).__init__( *args, **kwards )
        self.fields['libros'].queryset = Libro.objects.all()