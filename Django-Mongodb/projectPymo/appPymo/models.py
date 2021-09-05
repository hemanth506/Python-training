from django.db import models
from django.db.models.fields import CharField

# Create your models here.

class Student(models.Model):
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    domain = models.CharField(max_length=200)
    