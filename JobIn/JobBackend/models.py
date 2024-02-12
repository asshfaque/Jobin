from django.db import models


# Create your models here.


# Create your models here.
class CompanyDb(models.Model):
    companyName = models.CharField(max_length=50, null=True, blank=True)
    information = models.CharField(max_length=500, null=True, blank=True)
    country = models.CharField(max_length=30, null=True, blank=True)
    companyProfile = models.ImageField(upload_to="companyProfile", null=True, blank=True)


class jobDb(models.Model):
    companyName = models.CharField(max_length=30, null=True, blank=True)
    job = models.CharField(max_length=30, null=True, blank=True)
    jobDetails = models.CharField(max_length=100, null=True, blank=True)
    qualification = models.CharField(max_length=30, null=True, blank=True)
    experience = models.CharField(max_length=30, null=True, blank=True)
    date = models.CharField(max_length=30, null=True, blank=True)
    time = models.CharField(max_length=30, null=True, blank=True)
    location = models.CharField(max_length=30, null=True, blank=True)
    contactNumber = models.IntegerField(null=True, blank=True)


class CountryDb(models.Model):
    countryName = models.CharField(max_length=20, null=True, blank=True)
    location = models.CharField(max_length=20, null=True, blank=True)
    countryFlag = models.ImageField(upload_to="countryFlag", null=True, blank=True)
