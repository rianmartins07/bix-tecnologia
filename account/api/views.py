from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated

from account.api.serializers import *


__all__ = ('UserView', 'GroupView')

User = get_user_model()



class UserView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    filter_fields = [f.name for f in User._meta.get_fields()]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']
    

class GroupView(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [IsAuthenticated]
    filter_fields = [f.name for f in Group._meta.get_fields()]
    http_method_names = ['get', 'post', 'put', 'patch', 'head', 'options']

    def get_queryset(self):
        order_params = self.request.query_params.get('order_by', '')
        order_by = [param.strip() for param in order_params.split(',') if param]
        # tenant = self.request.tenant
        queryset = super(GroupView, self).get_queryset()  # .filter(tenant_id=tenant.pk)

        if order_by:
            queryset = queryset.order_by(*order_by)

        return queryset
