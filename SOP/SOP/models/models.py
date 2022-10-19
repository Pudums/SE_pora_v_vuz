from django.db import models


class User(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    is_student = models.BooleanField(default=False)
    group_id = models.IntegerField()


class Homeworks(models.Model):
    name = models.CharField(max_length=60)
    deadline = models.TimeField()
    content = models.TextField(max_length=1000)
    hw_id = models.IntegerField()


class Homework(models.Model):
    user_id = models.IntegerField()
    hw_id = models.IntegerField()
    grop_id = models.IntegerField()
    solution = models.TextField(max_length=10000)
    time = models.TimeField()