from django.db import models


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    active = models.BooleanField("Is student's account active?", default=True)
    health_group = models.ForeignKey("HealthGroup", on_delete=models.SET_NULL, null=True,
                                     verbose_name="Health group of a student")


class Trainer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    active = models.BooleanField("Is trainer's account active?", default=True)


class HealthGroup(models.Model):
    name = models.CharField(max_length=20)


class Group(models.Model):
    name = models.CharField(max_length=10)
    max_student_number = models.PositiveSmallIntegerField(default=20)
    trainers = models.ManyToManyField("Trainer", verbose_name="Trainers of the group")
    students = models.ManyToManyField("Student", verbose_name="Students enrolled in the group")
