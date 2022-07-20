from django.db import models

# Create your models here.
class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(verbose_name="Titulo", max_length=100)
    imagen = models.ImageField(upload_to='images/', verbose_name="Imagen", null=True)
    description = models.TextField(verbose_name="Descripcion", null=True)

    def __str__( self ):
        fila = "Titulo: " + self.titulo + " - " + "Descripcion " + self.description
        return fila

    def delete( self, using=None, keep_parents=False):
        self.imagen.storage.delete( self.imagen.name )
        super().delete()