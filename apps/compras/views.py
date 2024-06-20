from rest_framework import generics
from apps.compras.models import Comprador, Compra
from apps.compras.setializers import CompraSerializer, CompradorSerializer, CompraSerializer


class CompradorListCreate(generics.ListCreateAPIView):
    queryset = Comprador.objects.all()
    serializer_class = CompradorSerializer

class CompradorDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comprador.objects.all()
    serializer_class = CompradorSerializer

class CompraListCreate(generics.ListCreateAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer

class CompraDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Compra.objects.all()
    serializer_class = CompraSerializer