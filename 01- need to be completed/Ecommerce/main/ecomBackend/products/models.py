import uuid
from django.db import models
from django.contrib.postgres.fields import ArrayField

class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    meta_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Categories(BaseModel):
    name = models.CharField(max_length=50)
    images = models.ImageField(blank=True, null=True)

    def __str__(self):
        return f"Category ID: {self.id}, Name: {self.name}, images: {self.images}, meta_data: {self.meta_data}, created_at: {self.created_at}, updated_at: {self.updated_at}"


class Brand(BaseModel):
    name = models.CharField(max_length=50)
    description = models.TextField()


class Products(BaseModel):
    name = models.CharField(max_length=50)
    image = models.ImageField(blank=True, null=True)
    price = models.IntegerField()
    stock = models.IntegerField()
    category = models.ForeignKey(
        Categories, on_delete=models.CASCADE, default=None)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE, default=None)
