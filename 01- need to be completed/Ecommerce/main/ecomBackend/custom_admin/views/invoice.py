from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from custom_admin.routes import ROUTES


def create_invoice(request):
    try:
        return render(request, "invoice/create_invoice.html", ROUTES)
    except Exception as error:
        print(error)
        return render(request, "login.html")


def invoice_list(request):
    try:
        return render(request, "invoice/invoice_list.html", ROUTES)
    except Exception as error:
        print(error)
        return render(request, "login.html")


def invoice_preview(request):
    try:
        return render(request, "invoice/preview_invoice.html", ROUTES)
    except Exception as error:
        print(error)
        return render(request, "login.html")


def invoice_edit(request):
    try:
        return render(request, "invoice/edit_invoice.html", ROUTES)
    except Exception as error:
        print(error)
        return render(request, "login.html")


def invoice_print(request):
    try:
        return render(request, "file_manager.html", ROUTES)
    except Exception as error:
        print(error)
        return render(request, "login.html")
