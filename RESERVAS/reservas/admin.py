from django.contrib import admin
from .models import Sala, Reserva

@admin.register(Sala)
class SalaAdmin(admin.ModelAdmin):
    list_display = ('nombre', 'capacidad', 'ubicacion', 'equipo')

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ('usuario', 'sala', 'fecha_hora', 'duracion')