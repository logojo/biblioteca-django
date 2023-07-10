from django.db import models
from django.db.models import Q, Count, Avg, Sum
from django.db.models.functions import Lower



class PrestamoManager(models.Manager):
     
     def LibrosPromedioEdad(self):
         #en este caso con el doble guión bajo accedo a los campos de la tabla
         #y utilizo como referencia el campo relacionado
          result = self.filter(
               libro__id = '1'
          ).aggregate(
            #devuelve un dicionario de django con el promedio de edad de los lectores
             promedio_edad=Avg('lector__edad'),
             #agregando nuevo elemento al diccionario(array)
             suma_edad=Sum('lector__edad')
          )

          return result
     
    

     def numLibrosPrestamo(self):
          #devuelve un diccionario
          result = self.values(
               #estos son los campos que se utilizaran para la agrupacion, es este caso campo que hace la relacion en la tabla prestamos
               'libro'
          ).annotate(
               #para realizar el conteo de libros se utiliza el campo libro_prestamo que es el related_name que relaciona a la tabla prestamos con libros
               prestados = Count('libro'),
               titulo=Lower('libro__titulo')
          )

          for r in result:
               #Así se accede a los valores de un diccionario de django
               print(r, r['prestados'])

          return result