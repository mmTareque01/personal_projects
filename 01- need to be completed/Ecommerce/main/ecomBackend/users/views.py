from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Users
from .serializers import Users_Serializers, Users_Serializers_Short_Info
from custom_admin.routes import ROUTES
from django.contrib.auth.hashers import make_password

# Create your views here.


@api_view(["GET"])
def users(request, id):
    try:
        user = Users.objects.get(id=id)
        return Response({
            "status": 200,
            "message": "User retrieved successfully",
            "data": {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "user_name": user.user_name,
                "email": user.email,
                # "picture": user.picture, #this need to be fixed.
                "phone": user.phone,
                "address": user.address,
                "age": user.age,
                # Include other fields as needed
            }
        })

    except Users.DoesNotExist:
        return Response({
            "status": 404,
            "message": "User not found"
        })
    except Exception as e:
        return Response({
            "status": 500,
            "message": f"Error: {str(e)}"
        })


@api_view(["GET"])
def users_short_info(request, id):
    try:
        user = Users.objects.get(id=id)
        return Response({
            "status": 200,
            "message": "User retrieved successfully",
            "data": {
                "id": user.id,
                "first_name": user.first_name,
                "last_name": user.last_name,
                "user_name": user.user_name,
                "email": user.email,
                # "picture": user.picture, #this need to be fixed.
                "phone": user.phone,
                "address": user.address,
                "age": user.age,
                # Include other fields as needed
            }
        })

    except Users.DoesNotExist:
        return Response({
            "status": 404,
            "message": "User not found"
        })
    except Exception as e:
        return Response({
            "status": 500,
            "message": f"Error: {str(e)}"
        })


@api_view(["POST"])
def create_user(request):
    try:
        new_data = Users(
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name'),
            user_name=request.data.get('user_name'),
            email=request.data.get('email'),
            picture=request.data.get('picture'),
            phone=request.data.get('phone'),
            address=request.data.get('address'),
            age=request.data.get('age'),
            password=make_password(request.data.get("password"))
        )

        # Save the new user to the database
        new_data.save()
        print("createing users")
        return Response({
            "status": 200,
            "message": "trung to create data",
            "data": "created"
        })
    except Exception as e:
        print(e)
        return Response({
            "status": 200,
            "message": "trung to create data",
            "data": "eed"
        })


@api_view(["PUT"])
def update_user(request, id):
    try:
        new_data = Users(
            first_name=request.data.get('first_name'),
            last_name=request.data.get('last_name'),
            user_name=request.data.get('user_name'),
            email=request.data.get('email'),
            picture=request.data.get('picture'),
            phone=request.data.get('phone'),
            address=request.data.get('address'),
            age=request.data.get('age'),
            password=make_password(request.data.get("password"))
        )

        # Save the new user to the database
        new_data.save()
        print("createing users")
        return Response({
            "status": 200,
            "message": "trung to create data",
            "data": "created"
        })
    except Exception as e:
        print(e)
        return Response({
            "status": 200,
            "message": "trung to create data",
            "data": "eed"
        })


@api_view(["DELETE"])
def delete_user(request, id):
    try:
        user = Users.objects.get(id=id)
        user.delete()
        return Response({
            "status": 200,
            "message": "trung to create data",
            "data": "deleted"
        })
    except Exception as e:
        print(e)
        return Response({
            "status": 200,
            "message": "trung to create data",
            "data": "eed"
        })


def users_list(request):
    users = Users.objects.all()
    # serializer = Users_Serializers(users, many=True)
    return render(request, "users_list.html", {"users": users, "routes": ROUTES})
