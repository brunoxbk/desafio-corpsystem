from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from apps.estoque.models import Produto
from apps.compras.models import Comprador, Compra


class CompradorTests(APITestCase):

    def setUp(self):
        self.comprador_data = {'nome': 'Comprador Teste', 'email': 'comprador@teste.com'}
        self.comprador = Comprador.objects.create(**self.comprador_data)
        self.comprador_url = reverse('compras:comprador-detail', args=[self.comprador.id])
        self.compradores_url = reverse('compras:comprador-list-create')

    def test_listar_compradores(self):
        response = self.client.get(self.compradores_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_criar_comprador(self):
        new_comprador_data = {'nome': 'Novo Comprador', 'email': 'novo@comprador.com'}
        response = self.client.post(self.compradores_url, new_comprador_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreaterEqual(Comprador.objects.count(), 2)
        self.assertEqual(Comprador.objects.get(id=response.data['id']).nome, 'Novo Comprador')

    def test_obter_detalhes_comprador(self):
        response = self.client.get(self.comprador_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], self.comprador.nome)

    def test_atualizar_comprador(self):
        updated_comprador_data = {'nome': 'Comprador Atualizado', 'email': 'atualizado@comprador.com'}
        response = self.client.put(self.comprador_url, updated_comprador_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.comprador.refresh_from_db()
        self.assertEqual(self.comprador.nome, 'Comprador Atualizado')

    def test_excluir_comprador(self):
        total = Comprador.objects.count()
        response = self.client.delete(self.comprador_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Comprador.objects.count(), total - 1)



class CompraTests(APITestCase):

    def setUp(self):
        self.produto = Produto.objects.create(nome='Produto Teste', descricao='Descrição do produto teste', preco='10.50')
        self.comprador = Comprador.objects.create(nome='Comprador Teste', email='comprador@teste.com')
        self.compra_data = {'comprador': self.comprador, 'produto': self.produto, 'quantidade': 10, 'preco': '11.00'}
        self.compra = Compra.objects.create(**self.compra_data)
        self.compra_url = reverse('compras:compra-detail', args=[self.compra.id])
        self.compras_url = reverse('compras:compra-list-create')

    def test_listar_compras(self):
        response = self.client.get(self.compras_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_criar_compra(self):
        new_compra_data = {'comprador': self.comprador.id, 'produto': self.produto.id, 'quantidade': 5, 'preco': '14.00'}
        response = self.client.post(self.compras_url, new_compra_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Compra.objects.count(), 2)
        self.assertEqual(Compra.objects.get(id=response.data['id']).quantidade, 5)
        self.assertEqual(Compra.objects.get(id=response.data['id']).preco, 14.00)

    def test_obter_detalhes_compra(self):
        response = self.client.get(self.compra_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['quantidade'], self.compra.quantidade)
        self.assertEqual(response.data['preco'], str(self.compra.preco))

    def test_atualizar_compra(self):
        updated_compra_data = {'comprador': self.comprador.id, 'produto': self.produto.id, 'quantidade': 20, 'preco': '17.00'}
        response = self.client.put(self.compra_url, updated_compra_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.compra.refresh_from_db()
        self.assertEqual(self.compra.quantidade, 20)
        self.assertEqual(self.compra.preco, 17.00)

    def test_excluir_compra(self):
        response = self.client.delete(self.compra_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Compra.objects.count(), 0)
