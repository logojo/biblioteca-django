from django.db import models

#funcion de django que nos permite realizar acciones despues de guardar
from django.db.models.signals import post_save

from PIL import Image

from applications.autor.models import Autor
from .managers import LibroManager, CategoriaManager



# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=30)

    objects= CategoriaManager()

    def __str__(self):
        return  str(self.id) + ' - ' + self.nombre


class Libro(models.Model):
    categoria = models.ForeignKey(
        Categoria, 
        on_delete=models.CASCADE, 
        related_name='categoria_libro' #atributo que me sirve para llegar desde categorias a libros
    )
    #Relacion de muchos a muchos
    autores = models.ManyToManyField(Autor)
    titulo = models.CharField(max_length=50)
    fecha = models.DateField('Fecha de lanzamiento', auto_now=False, auto_now_add=False)
    portada = models.FileField(upload_to=None, max_length=100)
    visitas = models.PositiveIntegerField()
    stock = models.PositiveIntegerField(default=0)

    objects= LibroManager()

    #Metadatos
    #Un meta dato es todo aquello que no es un atributo del modelo o la tabla
    #Nos ayudan a personalizar el nombre, la apariencia en el administrador de django
    class Meta:
       verbose_name = 'Book'
       #verbose_name_plural = 'Libros' 
       ordering = ['titulo','fecha']

    def __str__(self):
        return  str(self.id) + ' - ' + self.titulo
    
# ============== end clase libro =========
    
def optimize_image(sender, instance, **kwords):
    if instance.portada:
        #accediento a imagen almacenada usando el Image del paquete pillow instalado con Pip
        portada = Image.open(instance.portada.path)
        #optimizando imagen a tamaño adecuado
        portada.save(instance.portada.path, quality=20, optimize=True)


#funciones que seran ejecutadas depues de guardar un libro
post_save.connect(optimize_image, sender=Libro)