from django.contrib import admin
from django.urls import path, include
from .views import system

urlpatterns = [
    # path("products/", include('products.urls')),
    path('', system),

]