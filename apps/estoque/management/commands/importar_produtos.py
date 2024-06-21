import requests
from django.core.management.base import BaseCommand
from apps.estoque.models import Produto, Estoque
from random import randint


class Command(BaseCommand):
    help = 'Importa produtos da API https://fakestoreapi.com/products'

    def handle(self, *args, **kwargs):
        url = 'https://fakestoreapi.com/products'
        response = requests.get(url)
        
        if response.status_code != 200:
            self.stdout.write(self.style.ERROR('Falha ao obter dados da API'))
            return
        
        produtos = response.json()
        
        for item in produtos:
            produto, created = Produto.objects.update_or_create(
                nome=item['title'],
                defaults={
                    'nome': item['title'],
                    'descricao': item['description'],
                    'preco': item['price'],
                    'categoria': item['category'],
                    'imagem': item['image']
                }
            )

            estoque, created = Estoque.objects.update_or_create(
                produto=produto,
                defaults={
                    'produto': produto,
                    'quantidade': randint(3,12)
                }

            )
            
            if created:
                self.stdout.write(self.style.SUCCESS(f'Produto {produto.nome} criado com sucesso'))
            else:
                self.stdout.write(self.style.SUCCESS(f'Produto {produto.nome} atualizado com sucesso'))
