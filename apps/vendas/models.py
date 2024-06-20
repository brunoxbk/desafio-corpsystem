from django.db import models

class Vendedor(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['-id']


class Venda(models.Model):
    vendedor = models.ForeignKey(Vendedor, on_delete=models.CASCADE)
    produto = models.ForeignKey('estoque.Produto', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Venda de {self.quantidade} {self.produto.nome} por {self.vendedor.nome} em {self.data}"
    
    class Meta:
        ordering = ['-id']
