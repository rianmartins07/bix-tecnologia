from django.db import models
from simple_history.models import HistoricalRecords

import shortuuid

from anuncio.models import Anuncio
# Create your models here.
class Reserva(models.Model):
    codigo_reserva = models.CharField(default=shortuuid.uuid, max_length=22, unique=True)
    check_in = models.DateField(null=False, blank=False)
    check_out = models.DateField(null=False, blank=False)
    valor = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2)
    comentario = models.TextField(max_length=512, null=True, blank=True)
    qtd_hospedes = models.IntegerField(null=False, blank=False)
    criado_em = models.DateTimeField(editable=False, auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)
    
    history = HistoricalRecords(
        history_id_field=models.BigAutoField(auto_created=True, primary_key=True, editable=False),
        related_name='historic',
        table_name='reserva_historic'
    )
    
    #foreign keys
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE, null=True)
    
    class Meta:
        managed=True
        db_table='reserva'