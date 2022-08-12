from distutils.command.upload import upload
from django.db import models

# Create your models here.
class  employee(models.Model):
    name = models.CharField('name',max_length=30)
    user = models.CharField('user',max_length=16)
    DOB = models.DateField('DOB')
    gender = models.CharField('gender',max_length=6)
    profile = models.ImageField(null=True,blank=True,upload_to ="images/")


