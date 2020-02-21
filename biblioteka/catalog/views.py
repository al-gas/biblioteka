from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world!<br/>You're at the Catalog Index.")
