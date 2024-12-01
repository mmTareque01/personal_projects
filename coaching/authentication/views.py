from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def authentication(request):
    return render(request, "index.html")

def login(request):
    return HttpResponse("this is login page")

def signUp(req):
    return HttpResponse("this is sign up page")

def forgotPassword(req):
    return HttpResponse("this is forgot password page!")