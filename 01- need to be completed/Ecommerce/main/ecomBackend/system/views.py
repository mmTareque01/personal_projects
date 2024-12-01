from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response



# Create your views here.
@api_view(["GET"])
def system(request):
    # users = Users.objects.all()
    # serializer = Users_Serializers(users, many=True)
    return Response({
        "status": 200,
        "message": "serializer.data"
    })


