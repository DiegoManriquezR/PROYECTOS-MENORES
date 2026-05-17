from django.shortcuts import render, get_object_or_404, redirect
from .models import Sala, Reserva
from .forms import SalaForm, ReservaForm
from django.db.models import Q
from django.contrib import messages
from datetime import timedelta
from django.utils import timezone
from django.core.exceptions import ValidationError

def inicio(request):
    """Vista de página de inicio"""
    return render(request, 'reservas/inicio.html')

def lista_salas(request):
    """Vista para listar salas con filtros de búsqueda"""
    q = request.GET.get('q', '').strip()
    min_cap = request.GET.get('cap', '').strip()
    
    salas = Sala.objects.all().order_by('nombre')
    
    
    if q:
        salas = salas.filter(
            Q(nombre__icontains=q) | 
            Q(equipo__icontains=q) | 
            Q(ubicacion__icontains=q)
        )

    if min_cap:
        try:
            minc = int(min_cap)
            if minc > 0:
                salas = salas.filter(capacidad__gte=minc)
        except (ValueError, TypeError):
            messages.warning(request, 'La capacidad debe ser un número válido.')
    
    return render(request, 'reservas/salas_list.html', {
        'salas': salas,
        'q': q,
        'cap': min_cap
    })

def crear_sala(request):
    """Vista para crear una nueva sala"""
    if request.method == 'POST':
        form = SalaForm(request.POST)
        if form.is_valid():
            try:
                sala = form.save()
                messages.success(request, f'Sala "{sala.nombre}" creada correctamente.')
                return redirect('lista_salas')
            except Exception as e:
                messages.error(request, 'Error al crear la sala. Intenta nuevamente.')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = SalaForm()
    
    return render(request, 'reservas/salas_form.html', {
        'form': form,
        'crear': True
    })

def editar_sala(request, pk):
    """Vista para editar una sala existente"""
    sala = get_object_or_404(Sala, pk=pk)
    
    if request.method == 'POST':
        form = SalaForm(request.POST, instance=sala)
        if form.is_valid():
            try:
                sala_actualizada = form.save()
                messages.success(request, f'Sala "{sala_actualizada.nombre}" actualizada correctamente.')
                return redirect('lista_salas')
            except Exception as e:
                messages.error(request, 'Error al actualizar la sala. Intenta nuevamente.')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = SalaForm(instance=sala)
    
    return render(request, 'reservas/salas_form.html', {
        'form': form,
        'crear': False,
        'sala': sala
    })

def eliminar_sala(request, pk):
    """Vista para eliminar una sala"""
    sala = get_object_or_404(Sala, pk=pk)
    
    if request.method == 'POST':
        try:
            nombre_sala = sala.nombre
            
            reservas_count = sala.reservas.count()
            if reservas_count > 0:
                messages.warning(
                    request, 
                    f'No se puede eliminar la sala "{nombre_sala}" porque tiene {reservas_count} reserva(s) asociada(s).'
                )
                return redirect('lista_salas')
            
            sala.delete()
            messages.success(request, f'Sala "{nombre_sala}" eliminada correctamente.')
            return redirect('lista_salas')
        except Exception as e:
            messages.error(request, 'Error al eliminar la sala. Intenta nuevamente.')
            return redirect('lista_salas')
    
    return render(request, 'reservas/salas_confirm_delete.html', {'sala': sala})

def lista_reservas(request):
    """Vista para listar reservas con filtros"""
    sala_id = request.GET.get('sala', '').strip()
    date_str = request.GET.get('fecha', '').strip()
    periodo = request.GET.get('periodo', 'all').strip()
    
    reservas = Reserva.objects.select_related('sala').all()
    
    # Filtro por sala
    if sala_id:
        try:
            sala_int = int(sala_id)
            reservas = reservas.filter(sala__id=sala_int)
        except (ValueError, TypeError):
            messages.warning(request, 'ID de sala inválido.')
    
    # Filtro por fecha
    if date_str:
        try:
            from datetime import datetime
            fecha = datetime.fromisoformat(date_str)
            reservas = reservas.filter(fecha_hora__date=fecha.date())
        except (ValueError, TypeError):
            messages.warning(request, 'Formato de fecha inválido.')
    
    # Filtro por período
    now = timezone.now()
    if periodo == 'past':
        reservas = reservas.filter(fecha_hora__lt=now)
    elif periodo == 'future':
        reservas = reservas.filter(fecha_hora__gte=now)
    
    return render(request, 'reservas/reservas_list.html', {
        'reservas': reservas,
        'salas': Sala.objects.all().order_by('nombre'),
        'selected_sala': sala_id,
        'fecha': date_str,
        'periodo': periodo
    })

def crear_reserva(request):
    """Vista para crear una nueva reserva"""
    if request.method == 'POST':
        form = ReservaForm(request.POST)
        if form.is_valid():
            try:
                # Verificar conflictos de horario
                sala = form.cleaned_data['sala']
                fecha = form.cleaned_data['fecha_hora']
                duracion = form.cleaned_data['duracion']
                
                start_new = fecha
                end_new = fecha + timedelta(minutes=duracion)
                
                # Buscar reservas existentes que puedan conflictuar
                existing_reservas = Reserva.objects.filter(sala=sala).exclude(
                    pk=form.instance.pk if hasattr(form.instance, 'pk') else None
                )
                
                conflicts = []
                for reserva_existente in existing_reservas:
                    start_existing = reserva_existente.fecha_hora
                    end_existing = start_existing + timedelta(minutes=reserva_existente.duracion)
                    
                    # Verificar si hay solapamiento
                    if (start_new < end_existing) and (end_new > start_existing):
                        conflicts.append(reserva_existente)
                
                if conflicts:
                    conflict_info = []
                    for conflict in conflicts:
                        conflict_info.append(
                            f"{conflict.usuario} ({conflict.fecha_hora.strftime('%d/%m/%Y %H:%M')})"
                        )
                    
                    messages.error(
                        request,
                        f'Conflicto de horario con las siguientes reservas: {", ".join(conflict_info)}'
                    )
                else:
                    reserva = form.save()
                    messages.success(
                        request,
                        f'Reserva para "{reserva.usuario}" en "{reserva.sala.nombre}" creada correctamente.'
                    )
                    return redirect('lista_reservas')
                    
            except Exception as e:
                messages.error(request, 'Error al crear la reserva. Intenta nuevamente.')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = ReservaForm()
    
    return render(request, 'reservas/reservas_form.html', {'form': form})

def editar_reserva(request, pk):
    """Vista para editar una reserva existente"""
    reserva = get_object_or_404(Reserva, pk=pk)
    
    if request.method == 'POST':
        form = ReservaForm(request.POST, instance=reserva)
        if form.is_valid():
            try:
                # Verificar conflictos de horario (excluyendo la reserva actual)
                sala = form.cleaned_data['sala']
                fecha = form.cleaned_data['fecha_hora']
                duracion = form.cleaned_data['duracion']
                
                start_new = fecha
                end_new = fecha + timedelta(minutes=duracion)
                
                existing_reservas = Reserva.objects.filter(sala=sala).exclude(pk=reserva.pk)
                
                conflicts = []
                for reserva_existente in existing_reservas:
                    start_existing = reserva_existente.fecha_hora
                    end_existing = start_existing + timedelta(minutes=reserva_existente.duracion)
                    
                    if (start_new < end_existing) and (end_new > start_existing):
                        conflicts.append(reserva_existente)
                
                if conflicts:
                    conflict_info = []
                    for conflict in conflicts:
                        conflict_info.append(
                            f"{conflict.usuario} ({conflict.fecha_hora.strftime('%d/%m/%Y %H:%M')})"
                        )
                    
                    messages.error(
                        request,
                        f'Conflicto de horario con las siguientes reservas: {", ".join(conflict_info)}'
                    )
                else:
                    reserva_actualizada = form.save()
                    messages.success(
                        request,
                        f'Reserva de "{reserva_actualizada.usuario}" actualizada correctamente.'
                    )
                    return redirect('lista_reservas')
                    
            except Exception as e:
                messages.error(request, 'Error al actualizar la reserva. Intenta nuevamente.')
        else:
            messages.error(request, 'Por favor corrige los errores en el formulario.')
    else:
        form = ReservaForm(instance=reserva)
    
    return render(request, 'reservas/reservas_form.html', {
        'form': form,
        'reserva': reserva
    })

def eliminar_reserva(request, pk):
    """Vista para cancelar/eliminar una reserva"""
    reserva = get_object_or_404(Reserva, pk=pk)
    
    if request.method == 'POST':
        try:
            info_reserva = f"{reserva.usuario} - {reserva.sala.nombre}"
            reserva.delete()
            messages.success(request, f'Reserva de "{info_reserva}" cancelada correctamente.')
            return redirect('lista_reservas')
        except Exception as e:
            messages.error(request, 'Error al cancelar la reserva. Intenta nuevamente.')
            return redirect('lista_reservas')
    
    return render(request, 'reservas/reservas_confirm_delete.html', {'reserva': reserva})