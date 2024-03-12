from django.test import TestCase
from django.urls import reverse
from rest_framework import status

from imovel.models import Imovel

class ImovelAPITestCase(TestCase):
    def setUp(self):
        self.imovel_obj = {
        "limite_hospedes": 1223,
        "qtd_banheiro": 1,
        "aceita_animais": False,
        "valor_limpeza": "50",
        "data_ativacao": "2024-03-07"
        }
        self.imovel = Imovel.objects.create(**self.imovel_obj)

    def test_imovel_listagem(self):
        url = reverse('imovel-listagem')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_imovel_criacao(self):
        url = reverse('imovel-listagem')
        
        response = self.client.post(url, data=self.imovel_obj, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_imovel_detalhe(self):
        url = reverse('imovel-detalhado', args=[self.imovel.pk])
        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_imovel_atualizacao_parcial(self):
        url = reverse('imovel-detalhado', args=[self.imovel.pk])
        data = {"valor_limpeza": '1231.00'} 
        response = self.client.patch(url, data=data, content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_imovel_delecao(self):
        url = reverse('imovel-detalhado', args=[self.imovel.pk])
        response = self.client.delete(url)

        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        with self.assertRaises(Imovel.DoesNotExist):
            Imovel.objects.get(pk=self.imovel.pk)
