import datetime #esta importacion es de python
from django.db import models
from django.db.models import Q, Count
#Importacion de extension trigram que mejora las consultas de busqueda en django
from django.contrib.postgres.search import TrigramSimilarity



class LibroManager(models.Manager):

    def listarLibros(self):
            return self.all()
    
    def buscarLibro(self, kword):
        result = self.filter(
            titulo__icontains = kword
        )
        return result
    
     # para utilizar trigram se requiere hacer la siguiente configuracion en la db
     #     crear extension en base de datos accediendo a tráves de la consola de postgres
     #     para poder utilizar la extension trigram para postgres
     #           create extension pg_trgm;

     #      despues se crea el indice para indicarle a la base de datos en que tabla va a realizar la busqueda
     #      todo en minisculas
     #      create index tabla_campo_idx on nombre_aplicacion_django_nombre_modelo using gin(nombre_del_campo gin_trgm_ops);
     # en necesario ingrasar un minimo de 3 caracteres
    def buscarLibroConTrigram(self, kword):
       if kword:
          result = self.filter(
               titulo__trigram_similar = kword
          )

          return result
       else:  
          return self.all()#[:10] ->para limitar el numero de registros


    
  
    
    
    def buscarLibroFecha(self, kword, fecha1, fecha2):

        #formatear fechas al tipo que  manaja el ORM de django en caso de dar un error
        #fecha1 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()
        #fecha2 = datetime.datetime.strptime(fecha1, "%Y-%m-%d").date()

        result = self.filter(
            titulo__icontains = kword,
            #consultas con rango de fechas
            fecha__range=(fecha1,fecha2)
        )
        return result
    
    #consulta con filtros de dos tablas relacionadas
    def listarLibrosCategoria(self, categoria):
         return self.filter(
              #busca libros por el id de categoria
              categoria__id=categoria
         ).order_by('titulo')
    

    def add_autor_libro(self, libro_id, autor):
         #se obtiene el libro de la bd en base al id enviado por fomulario
         libro = self.get(id=libro_id)
         #se agrega un nuevo autor al libro (solo se requiere mandar el id del autor)
         libro.autores.add(autor)      
         return libro

    def delete_autor_libro(self, libro_id, autor):
         #se obtiene el libro de la bd en base al id enviado por fomulario
         libro = self.get(id=libro_id)
         #se agrega un nuevo autor al libro (solo se requiere mandar el id del autor)
         libro.autores.remove(autor)      
         return libro    
  
    def librosPrestados(self):
         #aggregate se utiliza para realizar consultar aritmeticas a la bd
         #el aggregate devuelve un solo valor de la operacion
         #el annonate devuelve un query set de la operacion 
         result = self.aggregate(
              num_prestamos=Count('libro_prestamo')
         )

         return result;    
    
    #esta consulta es mejor realizarla desde la tabla prestamos ya que es donde se almacena esa informacion y es mas eficiente
    #contar el numero de veces que fue prestado libro, aqui utilizamos groupBy(annonate lo intuye automaticamente, utilizar el count) con django
    #values convierte la consulta en un diccionario
    def numLibrosPrestamo(self):
          #devuelve un diccionario
          result = self.values(
               #estos son los campos que se utilizaran para la agrupacion, es este caso campo que hace la relacion en la tabla prestamos
               'libro_prestamo'
          ).annotate(
               #para realizar el conteo de libros se utiliza el campo libro_prestamo que es el related_name que relaciona a la tabla prestamos con libros
               prestados = Count('libro_prestamo'),
          )

          #devuelve un queryset
          # result = self.annotate(
          #      #para realizar el conteo de libros se utiliza el campo libro_prestamo que es el related_name que relaciona a la tabla prestamos con libros
          #      prestados = Count('libro_prestamo')
          # )

          for r in result:
               print('*****')
               #Así se accede a los valores de un  querySet de django
               #print(r.titulo, r.fecha, r.visitas, r.prestados)

               #Así se accede a los valores de un diccionario de django
               print(r, r['prestados'])

          return result
    
class CategoriaManager(models.Manager):
     #consulta con filtros de tres tablas relacionadas
     def categoriaByAutor(self, autor):
          return self.filter(
             #Se extrae los libros en base al id del autor con su relacion con categorias
             categoria_libro__autores__id=autor
          ).distinct() #Esto es para que no te repita en este caso la categoria, como hacer un agrupamiento
     

     #Cuenta cuantos libros tiene cada categoria
     def LibrosByCategoria(self,):
          result = self.annotate(
               num_libros=Count('categoria_libro')
          )

          #Codigo solo para prueba

          for r in result:
               print('*******')
               print(r, r.num_libros)

          return result; 