# serializers.py
from rest_framework import serializers
from imovel.models import Imovel

class ImovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Imovel
        fields = '__all__'
