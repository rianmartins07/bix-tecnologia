# urls.py
from django.urls import path, re_path
from .views import ReservaDetalhadoView, ReservaListagemView

urlpatterns = [
    path('', ReservaListagemView.as_view(), name='reserva-listagem'),
    path('<int:pk>/', ReservaDetalhadoView.as_view(), name='reserva-detalhado'),
]
