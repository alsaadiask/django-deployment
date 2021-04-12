from django.db import models

# Create your models here.
class userinfo(models.Model):
    FirstName=models.CharField(max_length=128)
    LastName=models.CharField(max_length=128)
    email=models.EmailField()
    