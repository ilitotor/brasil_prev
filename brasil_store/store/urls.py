from django.conf.urls import url
from . import views


urlpatterns = [
    url(
        r'^api/v1/products/(?P<pk>[0-9]+)$',
        views.get_delete_update_product,
        name='get_delete_update_product'
    ),
    url(
        r'^api/v1/products/$',
        views.get_post_product,
        name='get_post_product'
    ),
    url(
        r'^api/v1/clients/(?P<pk>[0-9]+)$',
        views.get_delete_update_client,
        name='get_delete_update_client'
    ),
    url(
        r'^api/v1/clients/$',
        views.get_post_client,
        name='get_post_client'
    ),
    url(
        r'^api/v1/carts/(?P<pk>[0-9]+)$',
        views.get_delete_update_cart,
        name='get_delete_update_cart'
    ),
    url(
        r'^api/v1/carts/$',
        views.get_post_cart,
        name='get_post_cart'
    )

]