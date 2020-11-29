from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class bank_account(models.Model):
    user = models.ForeignKey(User, unique=False, on_delete=models.CASCADE)
    authCode = models.IntegerField()
    verified = models.BooleanField()
    accountID = models.IntegerField()
    telephoneNumber = models.IntegerField()
