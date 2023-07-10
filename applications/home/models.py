from django.db import models

# Create your models here.
class Persona(models.Model):
    nombre = models.CharField(max_length=50)
    apellidos = models.CharField(max_length=50)
    nacionalidad = models.CharField(max_length=30)
    edad = models.IntegerField()
    nickname = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'Persona'
        verbose_name_plural = 'Personas'

        #esto le indica al ORM con que nombre se creara la tabla en la db
        #esto nos es utilil para trabajar con bases de datos existentes
        db_table = 'persona'

        #el guión indica que se ordenara en orden inverso
        ordering = ['-nombre'] 

        #evita que se registren nombres duplicados o convinaciones de nombre de country de nickname 
        unique_together =  ('nacionalidad', 'nickname')        
        
        #restricciones
        constraints = [
            #validacion que evita que se registren personas menores a 18
            #gte representa a mayor o igual que
            #models.CheckConstraint(check=models.Q(edad__gte=18), name='adult')
        ]

        #Esto le indica a el ORM que es un modelo abstracto lo que significa que le heredara todos sus campos a las otras tablas
        #pero no se creara como una tabla en la BD
        abstract = True

    def __str__(self):
        return self.full_name
    
#Herencia
#Estoy heredando los campos del modelo persona
class Empleado(Persona):
    work = models.CharField(max_length=50)

# class Cliente(Persona):
#     email = models.EmailField(max_length=254)