#encoding:utf-8
from django.db import models
from imagekit.models import ImageSpecField
from imagekit.processors import ResizeToFill, ResizeToFit


class Categoria(models.Model):
    nombre = models.CharField(max_length=50)
    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural='Categorías'


class Imagen(models.Model):
    nombre = models.CharField(max_length=50)
    url = models.ImageField(upload_to='img', verbose_name='Imágen')
    imagen_thumbnail = ImageSpecField(source='url',
                                      processors=[ResizeToFit(700, 700)],
                                      format='PNG',
                                      options={'quality': 80})
    imagen_miniatura = ImageSpecField(source='url',
                                      processors=[ResizeToFill(50, 50)],
                                      format='PNG',
                                      options={'quality': 80})
    descripcion = models.TextField()
    categoria = models.ForeignKey(Categoria , verbose_name='Categoría')
   

    def __unicode__(self):
        return self.nombre
    class Meta:
        verbose_name_plural='Imágenes'
