from django.db import models

#managers
from .managers import AutorManager

# Create your models here.

class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    edad = models.PositiveBigIntegerField()

    def __str__(self):
        return self.nombre + ' ' + self.apellidos
    
    class Meta:
        #Esto le indica a el ORM que es un modelo abstracto lo que significa que le heredara todos sus campos a las otras tablas
        #pero no se creara como una tabla en la BD
        abstract =  True


#Herencia
#Estoy heredando los campos del modelo persona
class Autor(Persona):
    seudonimo = models.CharField(max_length=50, blank=True)
    #Se esta creando una asociacion con el archivo manager que se encargara de manaejar todas las funciones de
    #conexion a la base de datos
    objects = AutorManager()