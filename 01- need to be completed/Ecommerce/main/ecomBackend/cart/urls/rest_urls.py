from django.contrib import admin
from django.urls import path, include
from cart.views import create_cart, cart_list, delete_cart
from cart.routes import ROUTES

urlpatterns = [
    path(f"{ROUTES['create_cart']}", create_cart),
    path(f"{ROUTES['cart_list']}", cart_list),
    path("delete/<uuid>:id/", delete_cart),
    # path(ROUTES["user_list"], users_list),
    # path(ROUTES["user_list"], users_list),
    # path(ROUTES["user_list"], users_list),
]
