from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class UserProfileModel(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    month = models.CharField(max_length=20, null=False, blank=True)
    day = models.IntegerField(null=False,blank=True)
    year = models.IntegerField(null=False, blank=True)