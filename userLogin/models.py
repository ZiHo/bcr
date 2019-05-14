from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class userInfo(models.Model):
    name = models.CharField(max_length=10)
    passwd = models.CharField(max_length=30)
