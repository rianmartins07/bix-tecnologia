from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from datetime import date

from imovel.models import Imovel
from anuncio.models import Anuncio, Plataforma
from reserva.models import Reserva

class ReservaAPITestCase(TestCase):
    def setUp(self):
        self.plataforma = Plataforma.objects.create(nome_plataforma='Airbnb', taxa_plataforma=0.1)
        self.imovel = Imovel.objects.create(
            limite_hospedes=4,
            qtd_banheiro=2,
            aceita_animais=True,
            valor_limpeza='100.00',
            data_ativacao=date(2023, 1, 1)
        )
        self.anuncio = Anuncio.objects.create(imovel=self.imovel, plataforma=self.plataforma)

    def test_reserva_listagem(self):
        url = reverse('reserva-listagem')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reserva_criacao(self):
        url = reverse('reserva-listagem')
        data = {
            "check_in": "2024-03-07",
            "check_out": "2024-03-08",
            "valor": "1123.21",
            "comentario": "string",
            "qtd_hospedes": 11,
            "anuncio": self.anuncio.id
        }
        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_reserva_detalhado(self):
        reserva = Reserva.objects.create(anuncio=self.anuncio, check_in='2024-03-01', check_out='2024-03-10', valor=1123.21, qtd_hospedes= 11)
        url = reverse('reserva-detalhado', args=[reserva.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_reserva_delecao(self):
        reserva = Reserva.objects.create(anuncio=self.anuncio, check_in='2024-03-01', check_out='2024-03-10', valor=3212.21,  qtd_hospedes= 11)
        url = reverse('reserva-detalhado', args=[reserva.pk])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

