from django.db import models

# Create your models here.

class User(models.Model):
    pic = models.ImageField(upload_to='profiles')

class Thyrocare(models.Model):
    BUN = models.CharField(max_length=10)
    CS = models.CharField(max_length=10)
    UA = models.CharField(max_length=10)
    Ca = models.CharField(max_length=10)

