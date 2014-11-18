#encoding:utf-8
from django.db import models

# Create your models here.
class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural='Categorías'

class Imagenes(models.Model):
    nombre = models.CharField(max_length=50)
    url = models.ImageField(upload_to='img', verbose_name='Imágen')
    descripcion = models.TextField()
    categoria_id = models.ForeignKey(Categoria , verbose_name='Categoría')
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural='Imágenes'
