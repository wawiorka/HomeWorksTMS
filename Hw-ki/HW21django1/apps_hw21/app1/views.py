from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello!! Nice to meet you! This my app1")
