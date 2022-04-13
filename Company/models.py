from django.db import models

# Create your models here.


class CompanyDetails(models.Model):
    id = models.AutoField(primary_key=True)
    company_name = models.CharField(max_length=100, unique=True)
    city = models.CharField(max_length=100)
    established_year = models.IntegerField()
