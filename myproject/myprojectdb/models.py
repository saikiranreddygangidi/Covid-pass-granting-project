from django.db import models

# Create your models here.
class Reg(models.Model):
    username=models.CharField(max_length=200)
    password=models.CharField(max_length=200)
class User_status(models.Model):
    username=models.CharField(max_length=200,unique = True)
    status=models.CharField(max_length=200)