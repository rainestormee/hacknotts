from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)