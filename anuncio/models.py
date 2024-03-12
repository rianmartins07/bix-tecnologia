from django.db import models
from simple_history.models import  HistoricalRecords
from django.core.exceptions import PermissionDenied
# Create your models here.

from imovel.models import Imovel
 
class Plataforma(models.Model):
    nome_plataforma= models.TextField(max_length=256, default=None, null=True)
    taxa_plataforma = models.FloatField(default=None, null=True)

class Anuncio(models.Model):
    criado_em = models.DateTimeField(editable=False, auto_now_add=True)
    ultima_atualizacao = models.DateTimeField(auto_now=True)
    
    history = HistoricalRecords(
        history_id_field=models.BigAutoField(auto_created=True, primary_key=True, editable=False),
        related_name='historic',
        table_name='anuncio_historico'
    )
    #foreign key

    imovel = models.ForeignKey(Imovel, on_delete=models.SET_NULL,null=True)
    plataforma = models.ForeignKey(Plataforma, on_delete=models.CASCADE, null=True)

    def delete(self, *args, **kwargs):
        raise PermissionDenied("Delecao nao permitida")

    class Meta:
        managed=True
        db_table='anuncio'
