from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render


def pageNotFound(request):
    return HttpResponse("<h1>this is header tag</h1>")



def custom_page_not_found(request, exception):
    return render(request, '404.html', status=404)