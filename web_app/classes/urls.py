from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('profile/', views.profile, name='profile'),
    path('classes/', views.classes_page, name='classes'),
    path('classes/all/', views.all_classes_schedule, name='all_classes_schedule'),
    path('classes/my/', views.my_classes_schedule, name='my_classes_schedule'),
    path('group/<int:pk>', views.sport_group, name='sport_group'),
    path('groups/', views.groups, name='sport_groups'),
]