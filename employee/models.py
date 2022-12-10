from django.db import models

# Create your models here.
class Employees(models.Model):
    first_name = models.CharField(max_length=40)
    last_name = models.CharField(max_length=40)
    title = models.CharField(max_length=40)
    gender = models.CharField(max_length=30)
    age = models.IntegerField(default=0)
    