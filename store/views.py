from django.contrib.auth.models import User

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import Product, Client, Cart
from .serializers import ProductSerializer, ClientSerializer, CartSerializer

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single product
    if request.method == 'GET':
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    # delete a single product
    elif request.method == 'DELETE':
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single product
    elif request.method == 'PUT':
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_product(request):
    # get all product
    if request.method == 'GET':
        product = Product.objects.all()
        serializer = ProductSerializer(product, many=True)
        return Response(serializer.data)

    # insert a new record for a product
    elif request.method == 'POST':
        data = {
            'name': request.data.get('name'),
            'description': request.data.get('description'),
            'price': request.data.get('price')
        }
        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_client(request, pk):
    try:
        client = Client.objects.get(pk=pk)
    except Client.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single client
    if request.method == 'GET':
        serializer = ClientSerializer(client)
        return Response(serializer.data)
    # delete a single client
    elif request.method == 'DELETE':
        client.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single client
    elif request.method == 'PUT':
        serializer = ClientSerializer(client, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'POST'])
def get_post_client(request):
    # get all client
    if request.method == 'GET':
        client = Client.objects.all()
        serializer = ClientSerializer(client, many=True)
        return Response(serializer.data)

    # insert a new record for a Client
    elif request.method == 'POST':
        data = {
            'user': request.user.id,
            'first_name': request.data.get('first_name'),
            'last_name': request.data.get('last_name'),
            'street_address': request.data.get('street_address'),
            'city': request.data.get('city'),
            'state': request.data.get('state'),
            'zip': request.data.get('zip'),
            'phone': request.data.get('phone')
        }
        serializer = ClientSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'DELETE', 'PUT'])
def get_delete_update_cart(request, pk):
    try:
        cart = Cart.objects.get(pk=pk)
    except cart.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    # get details of a single client
    if request.method == 'GET':
        serializer = CartSerializer(cart)
        return Response(serializer.data)
    # delete a single client
    elif request.method == 'DELETE':
        cart.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    # update details of a single client
    elif request.method == 'PUT':
        serializer = CartSerializer(cart, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_204_NO_CONTENT)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'POST'])
def get_post_cart(request):
    # get all cart
    if request.method == 'GET':
        cart = Cart.objects.all()
        serializer = CartSerializer(cart, many=True)
        return Response(serializer.data)

    # insert a new record for a Cart
    elif request.method == 'POST':
        data = {
            'user': request.user.id,
            'items': request.data.get('item')
        }
        serializer = CartSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




# {
#     "first_name": "Ilito",
#     "last_name": "Torquato",
#     "street_address1": "Rua X, 433",
#     "city": "São Paulo",
#     "state": "São Paulo",
#     "zip": "04051-080",
#     "phone": "0000-2999"
# }
#
#  {
#     "name": "Milk",
#     "description": "Vegan Milk",
#     "price": 1.83
#  }

 # {
 #    "item": [1]
 # }
