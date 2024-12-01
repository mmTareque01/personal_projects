from django.contrib import admin
from .models import Products, Categories, Brand

# Register your models here.
admin.site.register(Products)
admin.site.register(Brand)
admin.site.register(Categories)
