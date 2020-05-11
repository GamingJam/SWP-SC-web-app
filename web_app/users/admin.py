from django.contrib import admin
from django.contrib.admin import ModelAdmin
from django.contrib.auth.admin import UserAdmin

from .forms import CustomUserCreationForm, CustomUserChangeForm
from .models import *


class CustomUserAdmin(UserAdmin):
    add_form = CustomUserCreationForm
    form = CustomUserChangeForm
    model = User
    list_display = ('email', 'is_staff', 'is_student', 'is_trainer', 'is_active')
    list_filter = ('is_staff', 'is_student', 'is_trainer', 'is_active')
    fieldsets = (
        (None, {'fields': ('email', 'password', 'first_name', 'last_name')}),
        ('Permissions', {'fields': ('is_staff', 'is_student', 'is_trainer', 'is_active')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2', 'first_name', 'last_name', 'is_staff', 'is_student', 'is_trainer', 'is_active')}
        ),
    )
    search_fields = ('email',)
    ordering = ('email',)


class ProfileAdmin(ModelAdmin):
    list_display = ('email', 'full_name',)


admin.site.register(User, CustomUserAdmin)
admin.site.register(StudentProfile, ProfileAdmin)
admin.site.register(TrainerProfile, ProfileAdmin)
