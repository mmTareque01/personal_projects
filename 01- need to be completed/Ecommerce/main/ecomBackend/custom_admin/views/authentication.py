from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.contrib import messages
from custom_admin.routes import ROUTES


def login_view(request):
    try:
        if request.method == "POST":
            username = request.POST.get("username")
            password = request.POST.get("user_password")
            user = authenticate(request, username=username, password=password)

            if user is not None:
                print("succeeded")
                login(request, user)  # This should now correctly call Django's login function
                return redirect('dashboard-view')
            else:
                print("failed")
                return render(request, "index.html", {"error": "Username or password didn't match!"})

        return render(request, 'login.html')
    except Exception as error:
        print(error)
        return render(request, 'login.html')


def dashboard(request):
    try:
        print(ROUTES['admin'])
        return render(request, "dashboard.html", {"routes":ROUTES})
    except Exception as error:
        print(error)
        return render(request, "login.html")
