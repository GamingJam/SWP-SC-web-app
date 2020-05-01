from django.db import models
from datetime import timedelta
from django.utils.timezone import localtime

from users.models import TrainerProfile as Trainer, StudentProfile as Student


class HealthGroup(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'health groups'
        ordering = ['id']


class SportGroup(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    max_student_number = models.PositiveSmallIntegerField(default=20)
    trainers = models.ManyToManyField(Trainer, verbose_name="Trainers of the group")
    students = models.ManyToManyField(Student, verbose_name="Students enrolled in the group")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date group was created")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'sport groups'
        ordering = ['id']


class SportClass(models.Model):
    group = models.ForeignKey(SportGroup, on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Date and time of the sport class")
    duration = models.DurationField(default=timedelta(hours=1, minutes=30), verbose_name="Duration of the class")

    def str_date(self):
        return localtime(self.date).strftime("%d %B")

    def str_time(self):
        return localtime(self.date).strftime("%H:%M")

    def __str__(self):
        return str(self.group) + " on " + self.str_date() + ", " + self.str_time()

    class Meta:
        verbose_name_plural = 'sport classes'
        ordering = ['date', 'group']


class Attendance(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    sport_class = models.ForeignKey(SportClass, on_delete=models.SET_NULL, null=True)
    presence = models.BooleanField(default=False, verbose_name="Was the student present in the class?")

    def __str__(self):
        return str(self.student) + " in class " + str(self.sport_class)

    class Meta:
        verbose_name_plural = 'attendance'
        ordering = ['id']
