from rest_framework import serializers
from .models import Users

class Users_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = "__all__"


class Users_Serializers_Short_Info(serializers.ModelSerializer):
    class Meta:
        model = Users
        exclude = ['created_at', 'updated_at', 'meta_data']
