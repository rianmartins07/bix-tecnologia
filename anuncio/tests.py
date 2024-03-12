from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient
from datetime import date

from anuncio.models import Anuncio, Plataforma
from imovel.models import Imovel

class AnuncioAPITestCase(TestCase):
    def setUp(self):
        self.plataforma = Plataforma.objects.create(nome_plataforma="Airbnb", taxa_plataforma=0.1)
        self.plataforma2 = Plataforma.objects.create(nome_plataforma="teste", taxa_plataforma=0.7)
        self.imovel = Imovel.objects.create(
            limite_hospedes=4,
            qtd_banheiro=2,
            aceita_animais=True,
            valor_limpeza="100.00",
            data_ativacao=date(2023, 1, 1)
        )
        self.anuncio = Anuncio.objects.create(imovel=self.imovel, plataforma=self.plataforma)

    def test_anuncio_listagem(self):
        url = reverse("anuncio-listagem")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anuncio_criacao(self):
        url = reverse("anuncio-listagem")
        response = self.client.post(url, data={"imovel": self.imovel.pk, "plataforma": self.plataforma.pk}, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_anuncio_detalhe(self):
        anuncio = Anuncio.objects.create(imovel=self.imovel, plataforma=self.plataforma)
        url = reverse("anuncio-detalhado", args=[anuncio.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_anuncio_atualizacao_parcial(self):
        url = reverse("anuncio-detalhado", args=[self.anuncio.pk])
        data = {"plataforma": self.plataforma2.pk}  # Use o ID da Plataforma
        response = self.client.patch(url, data=data, content_type="application/json")

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class PlataformaDetalhadoViewTest(TestCase):
    def setUp(self):
        self.plataforma = Plataforma.objects.create(nome_plataforma="Teste", taxa_plataforma=0.05)
        self.client = APIClient()

    def test_get_plataforma_detalhado(self):
        url = reverse("plataforma-detalhado", args=[self.plataforma.pk])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_plataforma_detalhado(self):
        url = reverse("plataforma-detalhado", args=[self.plataforma.pk])
        data = {
            "nome_plataforma": "NovoNome",
            "taxa_plataforma": 0.1
        }
        response = self.client.put(url, data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_plataforma_detalhado(self):
        url = reverse("plataforma-detalhado", args=[self.plataforma.pk])
        data = {"taxa_plataforma": 0.2}

        response = self.client.patch(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalid_put_plataforma_detalhado(self):
        url = reverse("plataforma-detalhado", args=[self.plataforma.pk])
        data = {"nome_plataforma": "nova plataforma", "taxa_plataforma": 0.1}
        response = self.client.put(url, data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_invalid_patch_plataforma_detalhado(self):
        url = reverse("plataforma-detalhado", args=[self.plataforma.pk])
        data = {"taxa_plataforma": "invalid_value"}
        response = self.client.patch(url, data, content_type="application/json")
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)