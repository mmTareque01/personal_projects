from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def login(request):
    return render(request, "index.html")


def sign_up(request):
    return render(request, "sign_up.html")


def forgot_password(request):
    return render(request, "forgot_password.html")


def reset_password(request):
    return render(request, "reset_password.html")
