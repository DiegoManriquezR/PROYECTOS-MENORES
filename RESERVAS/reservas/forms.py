from django import forms
from .models import Sala, Reserva
from django.utils import timezone
from django.core.exceptions import ValidationError

class SalaForm(forms.ModelForm):
    class Meta:
        model = Sala
        fields = ['nombre', 'capacidad', 'equipo', 'ubicacion']
        widgets = {
            'nombre': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light border-secondary',
                'placeholder': 'Ej: Sala de Conferencias A1'
            }),
            'capacidad': forms.NumberInput(attrs={
                'class': 'form-control bg-dark text-light border-secondary',
                'placeholder': 'Ej: 25',
                'min': '1'
            }),
            'equipo': forms.Textarea(attrs={
                'class': 'form-control bg-dark text-light border-secondary',
                'placeholder': 'Ej: Proyector, Pizarra digital, Sistema de audio',
                'rows': 3
            }),
            'ubicacion': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light border-secondary',
                'placeholder': 'Ej: Piso 2, Edificio Principal'
            })
        }
        labels = {
            'nombre': 'Nombre de la sala',
            'capacidad': 'Capacidad (número de personas)',
            'equipo': 'Equipamiento disponible',
            'ubicacion': 'Ubicación'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['equipo'].required = False
        self.fields['ubicacion'].required = False
    
    def clean_nombre(self):
        nombre = self.cleaned_data['nombre']
        qs = Sala.objects.filter(nombre__iexact=nombre)
        if self.instance.pk:
            qs = qs.exclude(pk=self.instance.pk)
        if qs.exists():
            raise ValidationError('Ya existe una sala con este nombre.')
        return nombre.title()
    
    def clean_capacidad(self):
        capacidad = self.cleaned_data['capacidad']
        if capacidad <= 0:
            raise ValidationError('La capacidad debe ser mayor a cero.')
        if capacidad > 1000:
            raise ValidationError('La capacidad no puede ser mayor a 1000 personas.')
        return capacidad

class ReservaForm(forms.ModelForm):
    class Meta:
        model = Reserva
        fields = ['usuario', 'sala', 'fecha_hora', 'duracion']
        widgets = {
            'usuario': forms.TextInput(attrs={
                'class': 'form-control bg-dark text-light border-secondary',
                'placeholder': 'Ej: Juan Pérez García'
            }),
            'sala': forms.Select(attrs={
                'class': 'form-select bg-dark text-light border-secondary'
            }),
            'fecha_hora': forms.DateTimeInput(attrs={
                'type': 'datetime-local',
                'class': 'form-control bg-dark text-light border-secondary',
                'step': '300'
            }),
            'duracion': forms.NumberInput(attrs={
                'class': 'form-control bg-dark text-light border-secondary',
                'placeholder': 'Ej: 60',
                'min': '15',
                'step': '15'
            })
        }
        labels = {
            'usuario': 'Nombre del usuario',
            'sala': 'Sala a reservar',
            'fecha_hora': 'Fecha y hora de inicio',
            'duracion': 'Duración (minutos)'
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['sala'].queryset = Sala.objects.all().order_by('nombre')
        self.fields['sala'].empty_label = "Selecciona una sala"
    
    def clean_fecha_hora(self):
        fecha_hora = self.cleaned_data['fecha_hora']
        now = timezone.now()
        if fecha_hora < now - timezone.timedelta(minutes=5):
            raise ValidationError(f'La fecha y hora debe ser futura. Fecha actual: {now.strftime("%d/%m/%Y %H:%M")}')
        one_year_later = now + timezone.timedelta(days=365)
        if fecha_hora > one_year_later:
            raise ValidationError('No se pueden hacer reservas con más de un año de anticipación.')
        hora = fecha_hora.hour
        dia_semana = fecha_hora.weekday()
        if dia_semana >= 5:
            raise ValidationError('Solo se pueden hacer reservas de lunes a viernes.')
        if hora < 8 or hora >= 20:
            raise ValidationError('Las reservas solo están permitidas entre 8:00 y 20:00.')
        return fecha_hora
    
    def clean_duracion(self):
        duracion = self.cleaned_data['duracion']
        if duracion < 15:
            raise ValidationError('La duración mínima es de 15 minutos.')
        if duracion > 480:
            raise ValidationError('La duración máxima es de 8 horas (480 minutos).')
        if duracion % 15 != 0:
            raise ValidationError('La duración debe ser múltiplo de 15 minutos.')
        return duracion
    
    def clean_usuario(self):
        usuario = self.cleaned_data['usuario'].strip().title()
        if len(usuario) < 3:
            raise ValidationError('El nombre debe tener al menos 3 caracteres.')
        if len(usuario) > 100:
            raise ValidationError('El nombre no puede tener más de 100 caracteres.')
        if not any(c.isalpha() for c in usuario):
            raise ValidationError('El nombre debe contener al menos una letra.')
        return usuario
    
    def clean(self):
        cleaned_data = super().clean()
        fecha_hora = cleaned_data.get('fecha_hora')
        duracion = cleaned_data.get('duracion')
        if fecha_hora and duracion:
            end_time = fecha_hora + timezone.timedelta(minutes=duracion)
            if end_time.hour > 20 or (end_time.hour == 20 and end_time.minute > 0):
                raise ValidationError(f'La reserva debe terminar antes de las 20:00. Tu reserva terminaría a las {end_time.strftime("%H:%M")}.')
        return cleaned_data