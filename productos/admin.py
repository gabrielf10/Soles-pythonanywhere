from productos.models import Categoria, Imagen
from django.contrib import admin
from imagekit.admin import AdminThumbnail
# Register your models here.
class ImagenAdmin(admin.ModelAdmin):
    imagen = AdminThumbnail(image_field='imagen_miniatura')
    list_display = ('nombre', 'categoria','imagen')
    

admin.site.register(Categoria)
admin.site.register(Imagen,ImagenAdmin)

