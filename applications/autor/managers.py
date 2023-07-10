from django.db import models
from django.db.models import Q

class AutorManager(models.Manager):
    #Manager para modelo autor

    def listarAutores(self):
        return self.all()
    
    def buscarAutor(self, kword):
        result = self.filter(
            nombre__icontains = kword
        )
        return result
    
    def CustomBuscarAutor(self, kword):
        result = self.filter(
            #La funcion Q me permite realizar busquedas de varios campos a la vez comparando la info que viene desde el form 
            #representa al OR
            Q(nombre__icontains = kword) |  Q(apellidos__icontains = kword)
        )
        return result
    
    def buscarAutorExclude(self, kword):
        #La funcion exclude permite excluir de la consulta registros segun el criterio dado
        result = self.filter(
            nombre__icontains = kword
        ).exclude(
            Q(edad__icontains=70) | Q(edad__icontains=65)
        )

        #se puede realizar un filtro sobre otro
        # result = self.filter(
        #     nombre__icontains = kword
        # ).filter(
        #     Q(edad__icontains=70) | Q(edad__icontains=65)
        # )

        return result
    

    def buscarAutorRangoEdad(self):
        result = self.filter(
            # gt equivale a mayor que y lt a menor que la como es para hacer un "AND" en la consulta
            edad__gt = 40,
            edad__lt = 50

        ).order_by('apellidos', 'nombre')
        return result