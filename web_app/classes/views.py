from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.forms import UserCreationForm
from .models import *


def index(request):
    return render(request, 'classes/dashboard.html')


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()

    context = {'form': form}
    return render(request, 'classes/register.html', context)


def login(request):
    context = {}
    return render(request, 'classes/login.html', context)


def classes_schedule(request):
    classes = SportClass.objects.all()
    context = {'classes': classes}
    return render(request, 'classes/classes_schedule.html', context)


def sport_group(request, pk):
    group = SportGroup.objects.get(id=pk)

    context = {'group': group}
    return render(request, 'classes/group.html', context)


def groups(request):
    groups = SportGroup.objects.all()
    context = {'groups': groups}
    return render(request, 'classes/groups.html', context)
