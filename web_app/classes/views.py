from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from .models import *


def home(request):
    return render(request, 'classes/home.html')


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
