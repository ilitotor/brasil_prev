import json
from rest_framework import status
from django import test
from django.test import TestCase
from django.urls import reverse
from ..models import Product, Client, Cart

from ..serializers import ProductSerializer, ClientSerializer, CartSerializer


# initialize the APIClient app
client = test.Client()


class GetSingleProductTest(TestCase):

    """ Test module for GET single product API """

    def setUp(self):
        self.milk = Product.objects.create(
            name='Milk', description='Vegan Milk', price=1.89)
        self.cheese = Product.objects.create(
            name='Cheese', description='Vegan Cheese', price=1.29)

    def test_get_valid_single_product(self):
        response = client.get(
            reverse('get_delete_update_product', kwargs={'pk': self.milk.pk}))
        product = Product.objects.get(pk=self.milk.pk)
        serializer = ProductSerializer(product)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_invalid_single_product(self):
        response = client.get(
            reverse('get_delete_update_product', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

class GetAllProductsTest(TestCase):
    """ Test module for GET all products API """

    def setUp(self):
        Product.objects.create(
            name='Milk', description='Vegan Milk', price=1.89)
        Product.objects.create(
            name='Cheese', description='Vegan Cheese', price=1.29)

    def test_get_all_products(self):
        # get API response
        response = client.get(reverse('get_post_product'))
        # get data from db
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        self.assertEqual(response.data, serializer.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
