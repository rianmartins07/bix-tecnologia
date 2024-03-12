# urls.py
from django.urls import path, re_path
from .views import ImovelDetalhadoView, ImovelListagemView

urlpatterns = [
    path('', ImovelListagemView.as_view(), name='imovel-listagem'),
    path('<int:pk>/', ImovelDetalhadoView.as_view(), name='imovel-detalhado'),
]
