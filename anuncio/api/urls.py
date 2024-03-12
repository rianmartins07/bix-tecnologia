# urls.py
from django.urls import path, re_path
from .views import *

urlpatterns = [
    path('', AnuncioListagemView.as_view(), name='anuncio-listagem'),
    path('<int:pk>/', AnuncioDetalhadoView.as_view(), name='anuncio-detalhado'),
    path('plataforma/', PlataformaListagemView.as_view(), name='plataforma-listagem'),
    path('plataforma/<int:pk>/', PlataformaDetalhadoView.as_view(), name='plataforma-detalhado'),
]
