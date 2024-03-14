from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import Group, Permission
from django.http import HttpResponse
from django.template import loader
from django.urls import reverse_lazy
from django.shortcuts import get_object_or_404



def login(request):
    html_template = loader.get_template(f'account/index.html')
    context = dict()
    return HttpResponse(html_template.render(context, request))