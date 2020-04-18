from django.db import models


class Student(models.Model):
    first_name = models.CharField(50)
    last_name = models.CharField(50)
    email = models.EmailField()
    active = models.BooleanField("Is student's account active?")
    health_group = models.ForeignKey("HealthGroup", on_delete=models.SET_NULL,
                                     verbose_name="Health group of a student")


class Trainer(models.Model):
    first_name = models.CharField(50)
    last_name = models.CharField(50)
    email = models.EmailField()
    active = models.BooleanField("Is trainer's account active?")


class HealthGroup(models.Model):
    name = models.CharField(20)


class Group(models.Model):
    name = models.CharField(10)
    max_student_number = models.PositiveSmallIntegerField(default=20)
    trainers = models.ManyToManyField("Trainer", verbose_name="Trainers of the group")
    students = models.ManyToManyField("Student", verbose_name="Students enrolled in the group")
