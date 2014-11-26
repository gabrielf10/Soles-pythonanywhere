from productos.models import Categoria, Imagen
from django.contrib import admin
from imagekit.admin import AdminThumbnail
# Register your models here.
class ImagenAdmin(admin.ModelAdmin):
    admin_thumbnail = AdminThumbnail(image_field='imagen_miniatura')
    list_display = ('nombre', 'categoria','admin_thumbnail')

admin.site.register(Categoria)
admin.site.register(Imagen,ImagenAdmin)

