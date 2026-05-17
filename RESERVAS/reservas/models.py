from django.db import models
from django.core.validators import MinValueValidator
class Sala(models.Model):
    nombre = models.CharField(max_length=100)
    capacidad = models.PositiveIntegerField(validators=[MinValueValidator(1)])
    equipo = models.CharField(max_length=200, blank=True)
    ubicacion = models.CharField(max_length=200, blank=True)
    def __str__(self):
        return self.nombre
class Reserva(models.Model):
    usuario = models.CharField(max_length=100)
    sala = models.ForeignKey(Sala, on_delete=models.CASCADE, related_name='reservas')
    fecha_hora = models.DateTimeField()
    duracion = models.PositiveIntegerField(help_text='Duración en minutos', validators=[MinValueValidator(1)])
    class Meta:
        ordering = ['-fecha_hora']
    def __str__(self):
        return f"Reserva {self.usuario} - {self.sala.nombre} @ {self.fecha_hora}"
    
    
    
