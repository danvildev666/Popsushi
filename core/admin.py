from django.contrib import admin

from core.models import Carrusel,Galeriap

class CarruselAdmin(admin.ModelAdmin):
    list_display = ['descripcion', 'foto']
    search_fields = ['descripcion']
    list_filter = ['descripcion']
    fields = ['image_tag']
    list_per_page = 10
    
   

admin.site.register(Carrusel,CarruselAdmin)
admin.site.register(Galeriap)