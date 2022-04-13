from rest_framework import generics
from .serializers import CompanySerializer
from .models import CompanyDetails
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class CompanyView(generics.GenericAPIView):
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]

    queryset = CompanyDetails.objects.all()
    lookup_field = 'id'

    def post(self, request):
        serializer = CompanySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=201)

    def get(self, request):
        return Response(CompanyDetails.objects.values('company_name', 'city', 'established_year'))


class CompanyDetailView(generics.GenericAPIView):
    serializer_class = CompanySerializer
    permission_classes = [AllowAny]

    queryset = CompanyDetails.objects.all()
    lookup_field = 'id'

    def get(self, request, id):
        return Response(CompanyDetails.objects.filter(id=id).values('company_name', 'city', 'established_year'))

    def patch(self, request, id):
        company = CompanyDetails.objects.get(id=id)
        serializer = CompanySerializer(
            company, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(CompanyDetails.objects.filter(id=id).values('company_name', 'city', 'established_year'))
