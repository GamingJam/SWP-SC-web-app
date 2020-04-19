from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    return render(request, 'classes/dashboard.html')


def register(request):
    context = {}
    return render(request, 'classes/register.html', context)


def login(request):
    context = {}
    return render(request, 'classes/login.html', context)