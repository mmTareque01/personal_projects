import uuid
from django.db import models

# Create your models here.
class Base_Model(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    meta_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Users(Base_Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    user_name = models.CharField(max_length=50, unique=True)
    email = models.EmailField(unique=True)
    picture = models.ImageField(blank=True, null=True)
    phone = models.CharField(max_length=20)
    address = models.TextField(blank=True, null=True)
    age = models.IntegerField(20)
    password = models.TextField()

