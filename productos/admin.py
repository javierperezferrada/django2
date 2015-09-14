from django.contrib import admin
from .models import producto

class productoInline(admin.TabularInline):
    model = producto
    extra = 3


class productoAdmin(admin.ModelAdmin):
  
    list_display = ('nombre', 'descripcion', 'p_neto')
    #inlines = [productoInline]
    #list_filter = ['p_neto']
    search_fields = ['descripcion']

admin.site.register(producto, productoAdmin)