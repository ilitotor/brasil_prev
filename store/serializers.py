from rest_framework import serializers
from .models import Client, Product, Cart


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = ('date_created', 'user', 'first_name', 'last_name',
                  'street_address', 'city', 'state', 'zip', 'phone')


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price')


class CartSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = ('date_created', 'user', 'items')