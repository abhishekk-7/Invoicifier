from django.db import models
from django.contrib.auth.models import User
from Company.models import CompanyDetails
# Create your models here.


class Users(User):
    company = models.ForeignKey(
        CompanyDetails, to_field='company_name', on_delete=models.CASCADE, null=True)
