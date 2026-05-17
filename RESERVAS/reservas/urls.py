from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('salas/', views.lista_salas, name='lista_salas'),
    path('salas/crear/', views.crear_sala, name='crear_sala'),
    path('salas/editar/<int:pk>/', views.editar_sala, name='editar_sala'),
    path('salas/eliminar/<int:pk>/', views.eliminar_sala, name='eliminar_sala'),
    path('reservas/', views.lista_reservas, name='lista_reservas'),
    path('reservas/crear/', views.crear_reserva, name='crear_reserva'),
    path('reservas/editar/<int:pk>/', views.editar_reserva, name='editar_reserva'),
    path('reservas/eliminar/<int:pk>/', views.eliminar_reserva, name='eliminar_reserva'),
]