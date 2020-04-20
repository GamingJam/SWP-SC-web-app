from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('classes/', views.classes_schedule, name='classes_schedule'),
    path('group/<int:pk>', views.sport_group, name='sport_group')
]