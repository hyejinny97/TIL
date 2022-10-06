from distutils.command.upload import upload
from pyexpat import model
from django.db import models

# Create your models here.
class Movie(models.Model):
    title = models.CharField(max_length=80)
    summary = models.TextField()
    running_time = models.IntegerField()
    imgfile = models.ImageField(null=True, upload_to='', blank=True)