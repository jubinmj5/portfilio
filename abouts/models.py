from django.db import models

# Create your models here.
class Resume(models.Model):
    title = models.CharField(max_length=200,null=True)
    img = models.ImageField(upload_to = "images/",null=True)
    filetype = models.CharField(max_length=50,null=True)
    status = models.IntegerField(null=True)
    
class Project(models.Model):
    title = models.CharField(max_length=255)
    description =models.CharField(max_length=255)
    image = models.ImageField(upload_to = "images/",null=True)
    urlls = models.CharField(max_length=2500)
    status = models.IntegerField()
    