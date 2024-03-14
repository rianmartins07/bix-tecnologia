from django.db import models
from simple_history.models import HistoricalRecords
from django.contrib.auth import get_user_model
from celery import shared_task
from django.conf import settings
from django.core.mail import send_mail
import shortuuid

from anuncio.models import Anuncio
# Create your models here.
user = get_user_model()
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
    cancelada=models.BooleanField(default=False, null=False, help_text='usuario cancelou reserva')
    data_cancelamento=models.DateField(null=True, blank=False, default=None)
    reserva_fechada = models.BooleanField(default=False, null=False, help_text='field para identificar quando mandou email ou cancelou ou terminou checkout')
    #foreign keys
    usuario = models.ForeignKey(user, on_delete=models.CASCADE, null=False)
    anuncio = models.ForeignKey(Anuncio, on_delete=models.CASCADE, null=True)
    
    def liberar_quarto(self,):
        send_mail_task(self.usuario.id, self.codigo_reserva)
        print('enviou')
        self.reserva_fechada = True
        self.save()
    class Meta:
        managed=True
        db_table='reserva'




@shared_task(bind=True)
def send_mail_task(self, user_instance_id, codigo_reserva):
    User = get_user_model()
    user_instance = User.objects.get(id=user_instance_id)

    if not isinstance(user_instance, User):
        raise ValueError("A instância fornecida não é uma instância válida do modelo de usuário.")

    user_email = user_instance.email
    send_mail(
        f'Reserva {codigo_reserva} foi cancelada',
        'Informamos que sua reserva foi cancelada, mais informações em www.bix.com.br',
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )

    print(f'E-mail enviado para {user_email}: Reserva concluída.')