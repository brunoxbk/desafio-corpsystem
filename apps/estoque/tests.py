from rest_framework import status
from rest_framework.test import APITestCase
from django.urls import reverse
from apps.estoque.models import Produto, Estoque


class ProdutoTests(APITestCase):

    def setUp(self):
        self.produto_data = {'nome': 'Produto Teste', 'descricao': 'Descrição do produto teste', 'preco': '10.50'}
        self.produto = Produto.objects.create(**self.produto_data)
        self.produto_url = reverse('estoque:produto-detail', args=[self.produto.id])
        self.produtos_url = reverse('estoque:produto-list-create')

    def test_listar_produtos(self):
        response = self.client.get(self.produtos_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertGreaterEqual(len(response.data), 1)

    def test_criar_produto(self):
        new_produto_data = {'nome': 'Novo Produto', 'descricao': 'Descrição do novo produto', 'preco': '20.00', 'categoria': 'teste', 'imagem': 'https://api.chucknorris.io/img/avatar/chuck-norris.png'}
        response = self.client.post(self.produtos_url, new_produto_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertGreaterEqual(Produto.objects.count(), 2)
        self.assertEqual(Produto.objects.get(id=response.data['id']).nome, 'Novo Produto')

    def test_obter_detalhes_produto(self):
        response = self.client.get(self.produto_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['nome'], self.produto.nome)

    def test_atualizar_produto(self):
        updated_produto_data = {'nome': 'Produto Atualizado', 'descricao': 'Descrição atualizada', 'categoria': 'teste', 'preco': '15.00', 'imagem': 'https://api.chucknorris.io/img/avatar/chuck-norris.png'}
        response = self.client.put(self.produto_url, updated_produto_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.produto.refresh_from_db()
        self.assertEqual(self.produto.nome, 'Produto Atualizado')

    def test_excluir_produto(self):
        response = self.client.delete(self.produto_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Produto.objects.count(), 0)


class EstoqueTests(APITestCase):

    def setUp(self):
        self.produto = Produto.objects.create(nome='Produto Teste', descricao='Descrição do produto teste', preco='10.50')
        self.estoque_data = {'produto': self.produto, 'quantidade': 100}
        self.estoque = Estoque.objects.create(**self.estoque_data)
        self.estoque_url = reverse('estoque:estoque-detail', args=[self.estoque.id])
        self.estoques_url = reverse('estoque:estoque-list-create')

    def test_listar_estoque(self):
        response = self.client.get(self.estoques_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['count'], 1)

    def test_criar_estoque(self):
        new_produto = Produto.objects.create(nome='Novo Produto', descricao='Descrição do novo produto', preco='20.00')
        new_estoque_data = {'produto': new_produto.id, 'quantidade': 50}
        response = self.client.post(self.estoques_url, new_estoque_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Estoque.objects.count(), 2)
        self.assertEqual(Estoque.objects.get(id=response.data['id']).produto.id, new_produto.id)

    def test_obter_detalhes_estoque(self):
        response = self.client.get(self.estoque_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['quantidade'], self.estoque.quantidade)

    def test_atualizar_estoque(self):
        updated_estoque_data = {'produto': self.produto.id, 'quantidade': 150}
        response = self.client.put(self.estoque_url, updated_estoque_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.estoque.refresh_from_db()
        self.assertEqual(self.estoque.quantidade, 150)

    def test_excluir_estoque(self):
        response = self.client.delete(self.estoque_url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Estoque.objects.count(), 0)
