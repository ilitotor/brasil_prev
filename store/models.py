from django.db import models


class Client(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        'auth.User',
        related_name="client",
        on_delete=models.CASCADE,
    )
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    street_address = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    zip = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, blank=True, null=True)


class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.FloatField()


class Cart(models.Model):
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(
        'auth.User',
        related_name="carts",
        on_delete=models.CASCADE)
    items = models.ManyToManyField(Product)
