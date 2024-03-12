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


from .serializers import AnuncioSerializer, PlataformaSerializer
from anuncio.models import Anuncio, Plataforma


class AnuncioListagemView(APIView):
    serializer_class=AnuncioSerializer
    def get(self, request, *args, **kwargs):
        anuncios = Anuncio.objects.all()
        serializer = self.serializer_class(anuncios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=AnuncioSerializer)
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            serializer = self.serializer_class(data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Dados inválidos'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AnuncioDetalhadoView(APIView):
    serializer_class=AnuncioSerializer
    def get(self, request, pk, *args, **kwargs):
        anuncio = get_object_or_404(Anuncio, pk=pk)
        serializer = self.serializer_class(anuncio, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=AnuncioSerializer)
    def put(self, request, pk, *args, **kwargs):
        try:
            serializer = self.serializer_class
            anuncio = get_object_or_404(Anuncio, pk=pk)
            data = request.data
            serializer = self.serializer_class(instance=anuncio, data=data, partial=False)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
        except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=AnuncioSerializer)
    def patch(self, request, pk, *args, **kwargs):
        try:
            anuncio = get_object_or_404(Anuncio, pk=pk)
            data = request.data
            serializer = self.serializer_class(instance=anuncio, data=data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



class PlataformaListagemView(APIView):
    serializer_class=PlataformaSerializer
    def get(self, request, *args, **kwargs):
        anuncios = Plataforma.objects.all()
        serializer = self.serializer_class(anuncios, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=PlataformaSerializer)
    def post(self, request, *args, **kwargs):
        try:
            data = request.data
            
            serializer = self.serializer_class(data=data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            else:
                return Response({'error': 'Dados inválidos'}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PlataformaDetalhadoView(APIView):
    serializer_class=PlataformaSerializer

    def get(self, request, pk, *args, **kwargs):
        anuncio = get_object_or_404(Plataforma, pk=pk)
        serializer = self.serializer_class(anuncio, many=False)
        return Response(serializer.data, status=status.HTTP_200_OK)

    @swagger_auto_schema(request_body=PlataformaSerializer)
    def put(self, request, pk, *args, **kwargs):
        try:
            serializer = self.serializer_class
            plataforma = get_object_or_404(Plataforma, pk=pk)
            data = request.data
            serializer = self.serializer_class(instance=plataforma, data=data, partial=False)
            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
        except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=PlataformaSerializer)
    def patch(self, request, pk, *args, **kwargs):
        try:
            plataforma = get_object_or_404(Plataforma, pk=pk)
            data = request.data
            serializer = self.serializer_class(instance=plataforma, data=data, partial=True)

            if serializer.is_valid():
                serializer.save()
                return Response(status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
