from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import PermissionDenied
from .serializers import AnuncioSerializer, PlataformaSerializer
from anuncio.models import Anuncio, Plataforma

from rest_framework.permissions import IsAuthenticated



class AnuncioListagemView(APIView):
    serializer_class=AnuncioSerializer
    permission_classes = (IsAuthenticated, )
    
    def get(self, request, *args, **kwargs):
        if request.user.has_perm('anuncio.view_anuncio'):
            anuncios = Anuncio.objects.all()
            serializer = self.serializer_class(anuncios, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise PermissionDenied
    @swagger_auto_schema(request_body=AnuncioSerializer)
    def post(self, request, *args, **kwargs):
        try:
            if request.user.has_perm('anuncio.add_anuncio'):
                data = request.data
                serializer = self.serializer_class(data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
                else:
                    print(serializer.errors)
                    return Response({'error': 'Dados inválidos'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                raise PermissionDenied
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)


class AnuncioDetalhadoView(APIView):
    serializer_class=AnuncioSerializer
    permission_classes = (IsAuthenticated, )

    def get(self, request, pk, *args, **kwargs):
        if request.user.has_perm('anuncio.view_anuncio'):
            anuncio = get_object_or_404(Anuncio, pk=pk)
            serializer = self.serializer_class(anuncio, many=False)

            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise PermissionDenied

    @swagger_auto_schema(request_body=AnuncioSerializer)
    def put(self, request, pk, *args, **kwargs):
        try:
            if request.user.has_perm('anuncio.add_anuncio'):
                serializer = self.serializer_class
                anuncio = get_object_or_404(Anuncio, pk=pk)
                data = request.data
                serializer = self.serializer_class(instance=anuncio, data=data, partial=False)
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_200_OK)
            else:
                raise PermissionDenied
        except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    @swagger_auto_schema(request_body=AnuncioSerializer)
    def patch(self, request, pk, *args, **kwargs):
        try:
            if request.user.has_perm('anuncio.change_anuncio'):
                anuncio = get_object_or_404(Anuncio, pk=pk)
                data = request.data
                serializer = self.serializer_class(instance=anuncio, data=data, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_200_OK)
            else:
                raise PermissionDenied
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)



class PlataformaListagemView(APIView):
    serializer_class=PlataformaSerializer
    permission_classes = [IsAuthenticated]

    def get(self, request, *args, **kwargs):
        if request.user.has_perm('plataforma.view_plataforma'):
            anuncios = Plataforma.objects.all()
            serializer = self.serializer_class(anuncios, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise PermissionDenied

    @swagger_auto_schema(request_body=PlataformaSerializer)
    def post(self, request, *args, **kwargs):
        try:
            if request.user.has_perm('plataforma.add_plataforma'):
                data = request.data
                
                serializer = self.serializer_class(data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(data=serializer.data, status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': 'Dados inválidos'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                raise PermissionDenied
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class PlataformaDetalhadoView(APIView):
    serializer_class=PlataformaSerializer
    permission_classes = (IsAuthenticated)

    def get(self, request, pk, *args, **kwargs):
        if request.user.has_perm('plataforma.view_plataforma'):
            anuncio = get_object_or_404(Plataforma, pk=pk)
            serializer = self.serializer_class(anuncio, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise PermissionDenied


    @swagger_auto_schema(request_body=PlataformaSerializer)
    def put(self, request, pk, *args, **kwargs):
        try:
            if request.user.has_perm('plataforma.add_plataforma'):
                serializer = self.serializer_class
                plataforma = get_object_or_404(Plataforma, pk=pk)
                data = request.data
                serializer = self.serializer_class(instance=plataforma, data=data, partial=False)
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_200_OK)
            else:
                raise PermissionDenied
        except Exception as e:
                return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    

    @swagger_auto_schema(request_body=PlataformaSerializer)
    def patch(self, request, pk, *args, **kwargs):
        try:
            if request.user.has_perm('plataforma.change_plataforma'):
                plataforma = get_object_or_404(Plataforma, pk=pk)
                data = request.data
                serializer = self.serializer_class(instance=plataforma, data=data, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_200_OK)
            else:
                raise PermissionDenied
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
