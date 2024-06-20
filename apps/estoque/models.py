from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True, null=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    categoria = models.CharField(max_length=50)
    imagem = models.URLField(max_length=100)
    
    def __str__(self):
        return self.nome
    
    class Meta:
        ordering = ['-id']


class Estoque(models.Model):
    produto = models.ForeignKey(Produto, on_delete=models.CASCADE)
    quantidade = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.produto.nome} - {self.quantidade}"
    
    class Meta:
        ordering = ['-id']