import json
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import get_object_or_404
from django.core.serializers import serialize
from django.core.serializers.json import DjangoJSONEncoder
from django.http import HttpResponse
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from drf_yasg.utils import swagger_auto_schema


from .serializers import ReservaSerializer
from reserva.models import Reserva
from anuncio.models import Anuncio


class ReservaListagemView(APIView):
    serializer_class=ReservaSerializer
    def get(self, request, *args, **kwargs):
        reservas = Reserva.objects.all()
        serializer = self.serializer_class(reservas, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=ReservaSerializer)
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            anuncio_id = data.get('anuncio')
            serializer = self.serializer_class(data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Dados inválidos'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ReservaDetalhadoView(APIView):
    serializer_class=ReservaSerializer
    def get(self, request, pk, *args, **kwargs):
        reserva = get_object_or_404(Reserva, pk=pk)
        serializer = self.serializer_class(reserva, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def delete(self, request, pk, *args, **kwargs):
        try:
            imovel = get_object_or_404(Reserva, pk=pk)
            imovel.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)