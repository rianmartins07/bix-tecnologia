from rest_framework.exceptions import PermissionDenied
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from celery import shared_task
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from django.conf import settings
from drf_yasg.utils import swagger_auto_schema


from .serializers import ReservaSerializer
from reserva.models import Reserva



class ReservaListagemView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class=ReservaSerializer

    def get(self, request, *args, **kwargs):
        if request.user.has_perm('reserva.view_reserva'):
            reservas = Reserva.objects.all()
            serializer = self.serializer_class(reservas, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise PermissionDenied

    @swagger_auto_schema(request_body=ReservaSerializer)
    def post(self, request, *args, **kwargs):
        try:
            if request.user.has_perm('reserva.add_reserva'):
                data = request.data
                anuncio_id = data.get('anuncio')
                serializer = self.serializer_class(data=data, partial=True)
                if serializer.is_valid():
                    reserva_instance = serializer.save()
                    async_task = send_mail_task.delay(request.user.id, reserva_instance.id)
                    print(request.user.id)
                    return Response(data={**serializer.data, 'celery': str(async_task), 'task': 'E-mail enviado em segundo plano.'}, status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                raise PermissionDenied
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ReservaDetalhadoView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class=ReservaSerializer
    def get(self, request, pk, *args, **kwargs):
        if request.user.has_perm('reserva.view_reserva'):
            reserva = get_object_or_404(Reserva, pk=pk)
            serializer = self.serializer_class(reserva, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise PermissionDenied
        
    @swagger_auto_schema(request_body=ReservaSerializer)
    def patch(self, request, pk, *args, **kwargs):
        try:
            if request.user.has_perm('reserva.change_reserva'):
                reserva = get_object_or_404(Reserva, pk=pk)
                data = request.data
                serializer = self.serializer_class(instance=reserva, data=data, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response({'error': str(serializer.errors)}, status=status.HTTP_400_BAD_REQUEST)
            else:
                raise PermissionDenied
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

    def delete(self, request, pk, *args, **kwargs):
        try:
            if request.user.has_perm('reserva.delete_reserva'):
                reserva = get_object_or_404(Reserva, pk=pk)
                reserva.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                raise PermissionDenied
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



@shared_task(bind=True)
def send_mail_task(self, user_instance_id, reserva_id):
    User = get_user_model()
    user_instance = User.objects.get(id=user_instance_id)

    if not isinstance(user_instance, User):
        raise ValueError("A instância fornecida não é uma instância válida do modelo de usuário.")

    user_email = user_instance.email
    print(settings.EMAIL_HOST_USER)
    send_mail(
        'Reserva Concluída',
        'Sua reserva foi concluída com sucesso.',
        settings.EMAIL_HOST_USER,
        [user_email],
        fail_silently=False,
    )

    print(f'E-mail enviado para {user_email}: Reserva concluída.')

