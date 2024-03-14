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
from rest_framework.permissions import IsAuthenticated
from drf_yasg.utils import swagger_auto_schema
from rest_framework.exceptions import PermissionDenied

from .serializers import ImovelSerializer
from imovel.models import Imovel


class ImovelListagemView(APIView):
    permission_classes = [IsAuthenticated]
    serializer_class=ImovelSerializer
    def get(self, request, *args, **kwargs):
        if request.user.has_perm('imovel.view_imovel'):
            imovels = Imovel.objects.all()
            serializer = self.serializer_class(imovels, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise PermissionDenied

    @swagger_auto_schema(request_body=ImovelSerializer)
    def post(self, request, *args, **kwargs):
        try:
            if request.user.has_perm('imovel.add_imovel'):
                data = request.data
                serializer = self.serializer_class(data=data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_201_CREATED)
                else:
                    return Response({'error': 'Dados inválidos'}, status=status.HTTP_400_BAD_REQUEST)
            else:
                raise PermissionDenied
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

class ImovelDetalhadoView(APIView):
    serializer_class=ImovelSerializer
    def get(self, request, pk, *args, **kwargs):
        if request.user.has_perm('imovel.view_imovel'):
            imovel = get_object_or_404(Imovel, pk=pk)
            serializer = self.serializer_class(imovel, many=False)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            raise PermissionDenied

    @swagger_auto_schema(request_body=ImovelSerializer)
    def put(self, request, pk, *args, **kwargs):
        try:
            if request.user.has_perm('imovel.add_imovel'):
                imovel = get_object_or_404(Imovel, pk=pk)
                data = request.data
                serializer = self.serializer_class(instance=imovel, data=data, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_200_OK)
                else:
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            else:
                raise PermissionDenied
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)

    @swagger_auto_schema(request_body=ImovelSerializer)
    def patch(self, request, pk, *args, **kwargs):
        try:
            if request.user.has_perm('imovel.change_imovel'):
                imovel = get_object_or_404(Imovel, pk=pk)
                data = request.data
                serializer = self.serializer_class(instance=imovel, data=data, partial=True)

                if serializer.is_valid():
                    serializer.save()
                    return Response(status=status.HTTP_200_OK)
            else:
                raise PermissionDenied
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk, *args, **kwargs):
        try:
            if request.user.has_perm('imovel.delete_imovel'):

                imovel = get_object_or_404(Imovel, pk=pk)
                imovel.delete()
                return Response(status=status.HTTP_204_NO_CONTENT)
            else:
                raise PermissionDenied
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)