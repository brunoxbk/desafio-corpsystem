# estoque/tests/test_views.py

from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from apps.estoque.models import Produto
from apps.vendas.models import Vendedor, Venda

class VendedorTests(APITestCase):

    def setUp(self):
        self.vendedor_data = {'nome': 'Vendedor Teste', 'email': 'vendedor@teste.com'}
        self.vendedor = Vendedor.objects.create(**self.vendedor_data)
        self.vendedor_url = reverse('vendas:vendedor-detail', args=[self.vendedor.id])
        self.vendedores_url = reverse('vendas:vendedor-list-create')

    def test_listar_vendedores(self):
        response = self.client.get(self.vendedores_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_criar_vendedor(self):
        new_vendedor_data = {'nome': 'Novo Vendedor', 'email': 'novo@vendedor.com'}
        response = self.client.post(self.vendedores_url, new_vendedor_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Vendedor.objects.count(), 2)
        self.assertEqual(Vendedor.objects.get(id=response.data['id']).nome, 'Novo Vendedor')

    def test_obter_detalhes_vendedor(self):
        response = self.client.get(self.vendedor_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], self.vendedor.nome)

    def test_atualizar_vendedor(self):
        updated_vendedor_data = {'nome': 'Vendedor Atualizado', 'email': 'atualizado@vendedor.com'}
        response = self.client.put(self.vendedor_url, updated_vendedor_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.vendedor.refresh_from_db()
        self.assertEqual(self.vendedor.nome, 'Vendedor Atualizado')

    def test_excluir_vendedor(self):
        response = self.client.delete(self.vendedor_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Vendedor.objects.count(), 0)


class VendaTests(APITestCase):

    def setUp(self):
        self.produto = Produto.objects.create(nome='Produto Teste', descricao='Descrição do produto teste', preco='10.50')
        self.vendedor = Vendedor.objects.create(nome='Vendedor Teste', email='vendedor@teste.com')
        self.venda_data = {'vendedor': self.vendedor, 'produto': self.produto, 'quantidade': 10, 'preco': '12.00'}
        self.venda = Venda.objects.create(**self.venda_data)
        self.venda_url = reverse('vendas:venda-detail', args=[self.venda.id])
        self.vendas_url = reverse('vendas:venda-list-create')

    def test_listar_vendas(self):
        response = self.client.get(self.vendas_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_criar_venda(self):
        new_venda_data = {'vendedor': self.vendedor.id, 'produto': self.produto.id, 'quantidade': 5, 'preco': '15.00'}
        response = self.client.post(self.vendas_url, new_venda_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Venda.objects.count(), 2)
        self.assertEqual(Venda.objects.get(id=response.data['id']).quantidade, 5)
        self.assertEqual(Venda.objects.get(id=response.data['id']).preco, 15.00)

    def test_obter_detalhes_venda(self):
        response = self.client.get(self.venda_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['quantidade'], self.venda.quantidade)
        self.assertEqual(response.data['preco'], str(self.venda.preco))

    def test_atualizar_venda(self):
        updated_venda_data = {'vendedor': self.vendedor.id, 'produto': self.produto.id, 'quantidade': 20, 'preco': '18.00'}
        response = self.client.put(self.venda_url, updated_venda_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.venda.refresh_from_db()
        self.assertEqual(self.venda.quantidade, 20)
        self.assertEqual(self.venda.preco, 18.00)

    def test_excluir_venda(self):
        response = self.client.delete(self.venda_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Venda.objects.count(), 0)


