from django.db import models
from django.db.models.signals import post_delete

from applications.libro.models  import Libro
from applications.autor.models import Persona


from .managers import PrestamoManager
from .signals import update_libro_stock
# Create your models here.

class Lector(Persona):
    class Meta:
        verbose_name = 'Lector'    
        verbose_name_plural = 'Lectores'

class Prestamo(models.Model):
    lector = models.ForeignKey(Lector, on_delete=models.CASCADE)
    libro = models.ForeignKey(
        Libro, 
        on_delete=models.CASCADE,
        related_name='libro_prestamo'
    )
    fecha_prestamo = models.DateField(auto_now=False, auto_now_add=False)
    fecha_devolucion = models.DateField(blank=True, null=True)
    devuelto = models.BooleanField()

    objects = PrestamoManager()

    #Esta funcion se ejecutara cada vez que se guarde un registro
    #ya sea desde una vista o desde el administrador
    #Es una forma de ejecutar funciones desde los modelos
    # def save(self, *args, **kwards):
    #     self.libro.stock =  self.libro.stock - 1
    #     self.libro.visitas =  self.libro.visitas + 1
    #     self.libro.save();

    #    super(Prestamo, self).save(*args, **kwards)

    def __str__(self):
        return self.libro.titulo

post_delete.connect(update_libro_stock, sender=Prestamo)
