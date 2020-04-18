from django.db import models
from datetime import timedelta


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    active = models.BooleanField("Is student's account active?", default=True)
    health_group = models.ForeignKey("HealthGroup", on_delete=models.SET_NULL, null=True,
                                     verbose_name="Health group of a student")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date account was created")


class Trainer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    active = models.BooleanField("Is trainer's account active?", default=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date account was created")


class HealthGroup(models.Model):
    name = models.CharField(max_length=20)


class Group(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200)
    max_student_number = models.PositiveSmallIntegerField(default=20)
    trainers = models.ManyToManyField("Trainer", verbose_name="Trainers of the group")
    students = models.ManyToManyField("Student", verbose_name="Students enrolled in the group")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date group was created")


class SportClass(models.Model):
    group = models.ForeignKey("Group", on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Date and time of the sport class")
    duration = models.DurationField(default=timedelta(hours=1, minutes=30), verbose_name="Duration of the class")


class Attendance(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    sport_class = models.ForeignKey("SportClass", on_delete=models.SET_NULL, null=True)
    presence = models.BooleanField(default=False, verbose_name="Was the student present in the class?")