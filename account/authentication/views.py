from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import redirect
from django.urls import reverse
from .serializers import MyTokenObtainPairSerializer


@swagger_auto_schema(request_body=MyTokenObtainPairSerializer)
class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        token = response.data["access"]

        if request.path == '/api/token/' and request.COOKIES.get('bearer'):
            return redirect(reverse('schema-swagger-ui'))
        else:
            response.set_cookie("bearer", token, httponly=True, secure=False)
            return response
