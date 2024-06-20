from rest_framework import generics
from apps.estoque.models import Produto, Estoque
from apps.estoque.serializers import ProdutoSerializer, EstoqueSerializer


class ProdutoListCreate(generics.ListCreateAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class ProdutoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

class EstoqueListCreate(generics.ListCreateAPIView):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer

class EstoqueDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Estoque.objects.all()
    serializer_class = EstoqueSerializer

