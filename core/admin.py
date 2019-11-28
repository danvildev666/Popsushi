from django.contrib import admin

from core.models import Carrusel,Galeriap,Menu,Reserva,Sucursal,Tipo

class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nombre','rut','sucursal','fecha_reserva']
    search_fields = ['rut']
    list_filter = ['sucursal']
    
    list_per_page = 10
    
   

admin.site.register(Carrusel)
admin.site.register(Galeriap)
admin.site.register(Menu)
admin.site.register(Reserva,ReservaAdmin)
admin.site.register(Sucursal)
admin.site.register(Tipo)