from rest_framework import generics
from apps.vendas.models import Vendedor, Venda
from apps.vendas.serializers import VendedorSerializer, VendaSerializer


class VendedorListCreate(generics.ListCreateAPIView):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

class VendedorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vendedor.objects.all()
    serializer_class = VendedorSerializer

class VendaListCreate(generics.ListCreateAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer

class VendaDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Venda.objects.all()
    serializer_class = VendaSerializer
