from rest_framework import serializers
from cart.models import Cart

class Cart_Serializers(serializers.ModelSerializer):
    class Meta:
        model = Cart
        fields = "__all__"


# class Cart_List_Serializers(serializers.ModelSerializer):
#     class Meta:
#         model = Cart
#         exclude = ['created_at', 'updated_at', 'meta_data']
