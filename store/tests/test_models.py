from django.test import TestCase
from ..models import Product


class ProductTest(TestCase):
    """ Test module for Product model """

    def setUp(self):
        Product.objects.create(
            name='Milk', description='Vegan Milk', price=1.89)
        Product.objects.create(
            name='Cheese', description='Vegan Cheese', price=1.29)

    def test_product_price_description(self):
        product_milk = Product.objects.get(name='Milk')
        product_cheese = Product.objects.get(name='Cheese')
        self.assertEqual(
            product_milk.price, 1.89)
        self.assertEqual(
            product_cheese.description, "Vegan Cheese")