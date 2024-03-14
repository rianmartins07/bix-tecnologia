# tasks.py
from celery import shared_task
from datetime import datetime, timedelta
from .models import Reserva

@shared_task
def verificar_liberar_quartos():
    agora = '2024-01-01'
    reservas_canceladas = Reserva.objects.filter(cancelada=True, reserva_fechada=False)
    reservas_check_out = Reserva.objects.filter(reserva_fechada=False, check_out__gte=agora)

    for reserva in reservas_canceladas:
        reserva.liberar_quarto()

    for reserva in reservas_check_out:
        reserva.liberar_quarto()
