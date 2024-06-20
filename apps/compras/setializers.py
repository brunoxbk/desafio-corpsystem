from rest_framework import serializers
from apps.compras.models import Compra, Comprador

class CompraSerializer(serializers.ModelSerializer):
    class Meta:
        model = Compra
        fields = '__all__'


class CompradorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comprador
        fields = '__all__'