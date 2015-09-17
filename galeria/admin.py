from django.contrib import admin
from .models import Imagen

class productoInline(admin.TabularInline):
    model = Imagen
    extra = 3


class imagenAdmin(admin.ModelAdmin):
  
    list_display = ('nombre', 'descripcion', 'imagen')
    #inlines = [productoInline]
    #list_filter = ['p_neto']
    search_fields = ['descripcion']

admin.site.register(Imagen, imagenAdmin)