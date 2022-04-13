from .models import CompanyDetails
from rest_framework import serializers


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyDetails
        fields = ('company_name', 'city', 'established_year')
