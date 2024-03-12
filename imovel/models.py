from django.db import models
from simple_history.models import HistoricalRecords
import shortuuid
# Create your models here.

class Imovel(models.Model):
    codigo_imovel = models.CharField(default=shortuuid.uuid, max_length=22, unique=True)
    limite_hospedes = models.IntegerField(null=True, blank=True, default=None)
    qtd_banheiro = models.IntegerField(null=True, blank=True, default=None)
    aceita_animais = models.BooleanField(default=False)
    valor_limpeza = models.DecimalField(null=False, blank=False, max_digits=10, decimal_places=2)
    data_ativacao = models.DateField(null=False, blank=False)

    criado_em = models.DateTimeField(editable=False, auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)

    history = HistoricalRecords(
        history_id_field=models.BigAutoField(auto_created=True, primary_key=True, editable=False),
        related_name='historic',
        table_name='imovel_historico'
    )