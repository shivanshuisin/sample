from __future__ import unicode_literals

from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class User(models.Model):
    username=models.CharField(max_length=20,unique=True)
    password = models.CharField(max_length=50)
    accesslevel = models.CharField(max_length=20)
    f_name = models.CharField(max_length=20)
    l_name=models.CharField(max_length=20)
    department = models.CharField(max_length=20)
    designation=models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    base_salary=models.IntegerField()
    bonus=models.IntegerField()

    def __str__(self):

        return self.f_name+' '+self.l_name+':'+self.accesslevel

class Message(models.Model):
    username=models.CharField(max_length=300,unique=False)
    message=models.CharField(max_length=300)





