from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from .models import *


def home(request):
    if request.user.is_authenticated:
        return redirect('profile')
    else:
        return redirect('login')


def classes_page(request):
    return redirect('all_classes_schedule')


def all_classes_schedule(request):
    classes = SportClass.objects.all()
    context = {'classes': classes}
    return render(request, 'classes/classes_schedule.html', context)


@login_required
def my_classes_schedule(request):
    if request.user.is_student:
        classes = SportClass.objects.filter(group__students__in=[request.user.studentprofile])
    elif request.user.is_trainer:
        classes = SportClass.objects.filter(group__trainers__in=[request.user.trainerprofile])
    else:
        return redirect('home')
    context = {'classes': classes}
    return render(request, 'classes/classes_schedule.html', context)


def sport_group(request, pk):
    group = SportGroup.objects.get(id=pk)

    context = {'group': group}
    return render(request, 'classes/group.html', context)


@login_required
def profile(request):
    return render(request, 'classes/profile.html')


def groups(request):
    groups = SportGroup.objects.all()
    context = {'groups': groups}
    return render(request, 'classes/groups.html', context)
