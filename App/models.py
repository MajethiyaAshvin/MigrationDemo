from django.db import models

# Create your models here.

from django.db import models

# Create your models here.


class Userss(models.Model):
    username=models.CharField(max_length=30)
    password = models.CharField(max_length=30)