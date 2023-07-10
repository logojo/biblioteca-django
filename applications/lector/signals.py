def update_libro_stock(sender, instance, **kwards):
    #Actualizando stock al eliminar
    instance.libro.stock = instance.libro.stock + 1
    instance.libro.visitas = instance.libro.visitas - 1
    instance.libro.save()