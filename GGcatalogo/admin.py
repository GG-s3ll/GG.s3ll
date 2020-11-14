from django.contrib import admin
from .models import Desarrollador, Genero, Juego, Idiomas, Inventario

# Register your models here.
admin.site.register(Idiomas)
admin.site.register(Genero)

@admin.register(Desarrollador)
class DesarrolladorAdmin(admin.ModelAdmin):
    list_display = ('Desarrollador', 'fecha_creacion')
    fields = [('Desarrollador'), 'fecha_creacion']

@admin.register(Juego)
class JuegoAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'Desarrollador', 'clasificacion')

@admin.register(Inventario)
class InventarioAdmin(admin.ModelAdmin):
    list_filter = ('estatus')
    fieldsets = (
        ('Juego', {
            'fields': ('juego', 'fecha_lanzamiento', 'Idiomas', 'codigo')
        }),
        ('Disponibilidad', {
            'fields': ('estatus')
        })
    )

