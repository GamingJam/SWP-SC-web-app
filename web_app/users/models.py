from django.contrib.auth.models import AbstractUser
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from .managers import CustomUserManager


class User(AbstractUser):
    username = None
    email = models.EmailField('email address', unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []
    objects = CustomUserManager()

    is_student = models.BooleanField('student status', default=False)
    is_trainer = models.BooleanField('trainer status', default=False)

    def __str__(self):
        return self.email

    def display_name(self):
        if (full_name := self.get_full_name()) == '':
            return self.email
        else:
            return full_name

    class Meta:
        ordering = ['id']


class StudentProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    health_group = models.ForeignKey('classes.HealthGroup', on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        return str(self.user.get_full_name())

    def sport_group(self):
        return self.sportgroup_set.first()

    def email(self):
        return self.user.email

    def full_name(self):
        return self.user.get_full_name()

    class Meta:
        ordering = ['user']


class TrainerProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)

    def __str__(self):
        return str(self.user)

    def sport_group(self):
        return self.sportgroup_set.first()

    def email(self):
        return self.user.email

    def full_name(self):
        return self.user.get_full_name()

    class Meta:
        ordering = ['user']


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        if instance.is_student:
            StudentProfile.objects.create(user=instance)
        if instance.is_trainer:
            TrainerProfile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    if hasattr(instance, 'studentprofile'):
        instance.studentprofile.save()
    if hasattr(instance, 'trainerprofile'):
        instance.trainerprofile.save()
