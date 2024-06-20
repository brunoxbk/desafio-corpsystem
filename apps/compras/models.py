from django.db import models

class Comprador(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['-id']

class Compra(models.Model):
    comprador = models.ForeignKey(Comprador, on_delete=models.CASCADE)
    produto = models.ForeignKey('estoque.Produto', on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()
    data = models.DateTimeField(auto_now_add=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Compra de {self.quantidade} {self.produto.nome} por {self.comprador.nome} em {self.data}"
    
    class Meta:
        ordering = ['-id']
