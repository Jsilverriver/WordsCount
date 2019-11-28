from django.http import HttpResponse
from django.shortcuts import render


def homepage(request):
    return render(request, "home.html", {"hithere": "This is html+python"})


def eggs(request):
    return HttpResponse("<h1>EGGS</h1>")
