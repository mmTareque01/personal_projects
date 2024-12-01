import uuid
from django.db import models
from django_enum import EnumField


class Media_Type(models.TextChoices):
    FACEBOOIK = "facebook"
    INSTAGRAM = "instagram"
    TWITTER = "twitter"
    PHONE = "phone"
    YOUTUBE = "youtube"
    TELEPHONE = "telephone"


class Contacts(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    media = EnumField(Media_Type, blank=True, null=True)
    value = models.CharField(max_length=50, blank=True, null=True)

    meta_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Otp(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)

    otp = models.IntegerField()
    email = models.EmailField()
    user_name = models.CharField(max_length=50)

    meta_data = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
