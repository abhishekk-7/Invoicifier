from rest_framework import serializers
from .models import InvoiceDetails
from Account.models import Users


class GenerateInvoiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvoiceDetails
        fields = ('id', 'invoice_amount', 'seller',
                  'buyer', 'settled', 'acknowledged')


# class UpdateInvoiceSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = InvoiceDetails
#         fields = ('id', 'acknowledged')
