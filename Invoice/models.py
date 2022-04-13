from django.db import models
from Company.models import CompanyDetails
from Account.models import Users
# Create your models here.


class InvoiceDetails(models.Model):
    id = models.AutoField(primary_key=True)
    invoice_amount = models.IntegerField()
    seller = models.ForeignKey(
        Users, on_delete=models.CASCADE, null=True)
    buyer = models.ForeignKey(
        CompanyDetails, on_delete=models.CASCADE, to_field='company_name', null=True)
    acknowledged = models.BooleanField(default=False)
    settled = models.BooleanField(default=False)

    def __str__(self):
        return str(self.id)
