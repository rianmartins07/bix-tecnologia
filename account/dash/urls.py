from django.urls import re_path
from account.dash.views import *


urlpatterns = [
    re_path(r'login/$', login, name='login'),
]
