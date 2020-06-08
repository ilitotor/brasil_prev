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

class UpdateSingleProductTest(TestCase):
    """ Test module for updating an existing product record """

    def setUp(self):
        self.milk = Product.objects.create(
            name='Milk', description='Vegan Milk', price=1.89)
        self.cheese = Product.objects.create(
            name='Cheese', description='Vegan Cheese', price=1.29)
        self.valid_payload = {
            'name': 'Milk',
            'description': 'Vegan Milk',
            'price': 1.89,
        }
        self.invalid_payload = {
            'name': '',
            'description': 'Vegan Milk',
            'price': 1.89,
        }

    def test_valid_update_product(self):
        response = client.put(
            reverse('get_delete_update_product', kwargs={'pk': self.milk.pk}),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_update_product(self):
        response = client.put(
            reverse('get_delete_update_product', kwargs={'pk': self.cheese.pk}),
            data=json.dumps(self.invalid_payload),
            content_type='application/json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

class CreateNewProductTest(TestCase):

    """ Test module for inserting a new product """

    def setUp(self):
        self.valid_payload = {
            'name': 'Milk',
            'description': 'Vegan Milk',
            'price': 1.89,
        }
        self.invalid_payload = {
            'name': '',
            'description': 'Vegan Milk',
            'price': 1.89,
        }

    def test_create_valid_product(self):
        response = client.post(
            reverse('get_post_product'),
            data=json.dumps(self.valid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_create_invalid_product(self):
        response = client.post(
            reverse('get_post_product'),
            data=json.dumps(self.invalid_payload),
            content_type='application/json'
        )
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class DeleteSingleProductTest(TestCase):
    """ Test module for deleting an existing product record """

    def setUp(self):
        self.milk = Product.objects.create(
            name='Milk', description='Vegan Milk', price=1.89)

    def test_valid_delete_product(self):
        response = client.delete(
            reverse('get_delete_update_product', kwargs={'pk': self.milk.pk}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

    def test_invalid_delete_product(self):
        response = client.delete(
            reverse('get_delete_update_product', kwargs={'pk': 30}))
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)