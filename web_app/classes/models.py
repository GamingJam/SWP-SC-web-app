from django.db import models
from datetime import timedelta
from django.utils.timezone import localtime


class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    health_group = models.ForeignKey("HealthGroup", on_delete=models.SET_NULL, null=True, blank=True,
                                     verbose_name="Health group of a student")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date and time account was created")

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = 'students'


class Trainer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    active = models.BooleanField(default=True)
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date and time account was created")

    def __str__(self):
        return self.first_name + " " + self.last_name

    class Meta:
        verbose_name_plural = 'trainers'


class HealthGroup(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'health groups'


class SportGroup(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=200, null=True, blank=True)
    max_student_number = models.PositiveSmallIntegerField(default=20)
    trainers = models.ManyToManyField("Trainer", verbose_name="Trainers of the group")
    students = models.ManyToManyField("Student", verbose_name="Students enrolled in the group")
    date_created = models.DateTimeField(auto_now_add=True, verbose_name="Date group was created")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'sport groups'


class SportClass(models.Model):
    group = models.ForeignKey("SportGroup", on_delete=models.CASCADE)
    date = models.DateTimeField(verbose_name="Date and time of the sport class")
    duration = models.DurationField(default=timedelta(hours=1, minutes=30), verbose_name="Duration of the class")

    def __str__(self):
        return str(self.group) + " on " + localtime(self.date).strftime("%d %B, %H:%M")

    class Meta:
        verbose_name_plural = 'sport classes'


class Attendance(models.Model):
    student = models.ForeignKey("Student", on_delete=models.CASCADE)
    sport_class = models.ForeignKey("SportClass", on_delete=models.SET_NULL, null=True)
    presence = models.BooleanField(default=False, verbose_name="Was the student present in the class?")

    def __str__(self):
        return str(self.student) + " in class " + str(self.sport_class)

    class Meta:
        verbose_name_plural = 'attendance'
