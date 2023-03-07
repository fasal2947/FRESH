from django.db import models


# Create your models here.


class CustomerDetails(models.Model):
    username = models.CharField(max_length=100, null=True, blank=True)
    email = models.CharField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    confirmpassword = models.CharField(max_length=100, null=True, blank=True)


class checkkoutdb(models.Model):
    Fname = models.CharField(max_length=100, null=True, blank=True)
    Lname = models.CharField(max_length=100, null=True, blank=True)
    Email = models.CharField(max_length=100, null=True, blank=True)
    Address = models.CharField(max_length=100, null=True, blank=True)
    Landmark = models.CharField(max_length=100, null=True, blank=True)
    state = models.CharField(max_length=100, null=True, blank=True)
    city = models.CharField(max_length=100, null=True, blank=True)
    Pin = models.IntegerField(null=True, blank=True)




