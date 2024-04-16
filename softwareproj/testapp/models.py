from django.db import models

# Create your models here.
class Hydjobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
class Bangjobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
class Chennaijobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
class Kolkatajobs(models.Model):
    date = models.DateField()
    company = models.CharField(max_length=60)
    title = models.CharField(max_length=60)
    address = models.CharField(max_length=60)
    email = models.EmailField()
    phonenumber = models.BigIntegerField()
