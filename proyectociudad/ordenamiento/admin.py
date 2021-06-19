from django.contrib import admin

from ordenamiento.models import Parroquia, Barrio

class ParroquiaAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'tipo_parroquia')
    search_fields = ('nombre', 'tipo_parroquia')

admin.site.register(Parroquia, ParroquiaAdmin)


class BarrioAdmin(admin.ModelAdmin):

    list_display = ('nombre', 'num_viviendas', 'num_edificios', 'num_parques', 'parroquia')
    raw_id_fields = ('parroquia',)

admin.site.register(Barrio, BarrioAdmin)
