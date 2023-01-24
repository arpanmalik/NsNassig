from django.db import models
from django.contrib.auth.models import User
# Create your models here.

WORK_TYPE = (
    ('Youtube', 'Youtube'),
    ('Instagram', 'Instagram'),
    ('Other', 'Other'),
)

class Client(models.Model):
    name = models.CharField(max_length=100)
    user_instance = models.ForeignKey(User, on_delete=models.CASCADE)

class Work(models.Model):
    link = models.URLField(max_length=200)
    wort_type = models.CharField(choices=WORK_TYPE, max_length=100)


class Artist(models.Model):
    name = models.CharField(max_length=100)
    work = models.ManyToManyField(Work)
