from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('classes/', views.classes_schedule, name='classes_schedule'),
    path('group/<int:pk>', views.sport_group, name='sport_group'),
    path('groups/', views.groups, name='sport_groups'),
]