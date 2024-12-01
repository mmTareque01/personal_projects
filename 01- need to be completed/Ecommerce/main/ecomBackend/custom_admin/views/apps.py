from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from custom_admin.routes import ROUTES


def email(request):
    try:
        return render(request, "email.html", ROUTES)
    except Exception as error:
        print(error)
        return render(request, "login.html")


def chat(request):
    try:
        return render(request, "chat.html", ROUTES)
    except Exception as error:
        print(error)
        return render(request, "login.html")


def todo(request):
    try:
        return render(request, "todo.html", ROUTES)
    except Exception as error:
        print(error)
        return render(request, "login.html")


def calendar(request):
    try:
        return render(request, "calendar.html", ROUTES)
    except Exception as error:
        print(error)
        return render(request, "login.html")


def kanban(request):
    try:
        return render(request, "kanban.html", ROUTES)
    except Exception as error:
        print(error)
        return render(request, "login.html")


def file_manger(request):
    try:
        return render(request, "file_manager.html", ROUTES)
    except Exception as error:
        print(error)
        return render(request, "login.html")
