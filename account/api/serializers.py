from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.http.request import QueryDict
from rest_framework import serializers
import json

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        validated_data['is_active'] = True
        validated_data['is_superuser'] = False
        validated_data['is_staff'] = False

        instance = super(UserSerializer, self).create(validated_data)
        instance.save()

        return instance


    @property
    def email(self):
        return self.initial_data.get('email')

    @property
    def username(self):
        return self.initial_data.get('username')

    class Meta:
        model = User
        fields = '__all__'


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = '__all__'