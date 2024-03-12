# myapp/serializers.py
from rest_framework.authtoken.serializers import AuthTokenSerializer
from account.models import Token

class CustomAuthTokenSerializer(AuthTokenSerializer):
    class Meta:
        model = Token
        fields = ('key', 'user_type')