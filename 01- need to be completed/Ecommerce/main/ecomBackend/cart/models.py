import uuid
from django.db import models
from products.models import Products
from users.models import Users


class Base_Model(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    meta_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Cart(Base_Model):
    total = models.IntegerField()
    products = models.ForeignKey(
        Products, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(Users, on_delete=models.CASCADE, default=None)
