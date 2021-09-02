from django.db import models

# Create your models here.
class CheJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    tittle = models.CharField(max_length=30)
    eligbility = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phoneno = models.IntegerField()

class BanJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    tittle = models.CharField(max_length=30)
    eligbility = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phoneno = models.IntegerField()

class HydJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    tittle = models.CharField(max_length=30)
    eligbility = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phoneno = models.IntegerField()

class PuneJobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=30)
    tittle = models.CharField(max_length=30)
    eligbility = models.CharField(max_length=30)
    address = models.CharField(max_length=50)
    email = models.EmailField()
    phoneno = models.IntegerField()