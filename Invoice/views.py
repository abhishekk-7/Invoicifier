from rest_framework import generics
from .models import InvoiceDetails
from Account.models import Users
from .serializers import GenerateInvoiceSerializer
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
# Create your views here.


class InvoiceView(generics.GenericAPIView):
    serializer_class = GenerateInvoiceSerializer
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = GenerateInvoiceSerializer(data=request.data)
        seller = serializer.initial_data['seller']
        seller = Users.objects.filter(
            id=seller).values('company')[0]['company']
        print(seller)
        serializer.is_valid(raise_exception=True)
        if seller == serializer.initial_data['buyer']:
            return Response({"Error": "Seller and Buyer cannot be same"}, status=400)
        if 'acknowledged' in serializer.initial_data and serializer.initial_data['acknowledged']:
            return Response({"Error": "Seller can't mark acknowledged to true"}, status=400)
        serializer.save()
        return Response(serializer.data, status=201)

    def get(self, request):
        try:
            user = Users.objects.get(auth_token=request.headers['token'])
        except:
            return Response({"Error": "Invalid Token"}, status=400)
        return Response({"Invoices to company": InvoiceDetails.objects.filter(buyer=user.company.company_name).values('id', 'invoice_amount', 'seller', 'buyer', 'acknowledged', 'settled'),
                         "Invoices from company": InvoiceDetails.objects.filter(seller__company__company_name=user.company.company_name).values('id', 'invoice_amount', 'seller', 'buyer', 'acknowledged', 'settled')})


class InvoiceDetailView(generics.GenericAPIView):
    serializer_class = GenerateInvoiceSerializer
    permission_classes = [AllowAny]

    def get(self, request, id):
        return Response(InvoiceDetails.objects.filter(id=id).values('id', 'invoice_amount', 'seller', 'buyer', 'acknowledged', 'settled'))

    def patch(self, request, id):

        invoice = InvoiceDetails.objects.get(id=id)
        serializer = GenerateInvoiceSerializer(
            invoice, data=request.data, partial=True)
        seller = serializer.initial_data['seller']
        seller = Users.objects.filter(
            id=seller).values('company')[0]['company']
        if seller == serializer.initial_data['buyer']:
            return Response({"Error": "Seller and Buyer cannot be same"}, status=400)
        if 'acknowledged' in serializer.initial_data and serializer.initial_data['acknowledged'] != invoice.acknowledged:
            if 'token' not in request.headers:
                return Response({"Error": "Token is required"}, status=400)
            try:
                user = Users.objects.get(auth_token=request.headers['token'])
            except:
                return Response({"Error": "Invalid Token"}, status=400)
            print(user.company.company_name)
            if user.company.company_name != serializer.initial_data['buyer']:
                return Response({"Error": "You are not authorized to update this invoice"}, status=400)

        if 'settled' in serializer.initial_data and serializer.initial_data['settled'] != invoice.settled:
            if 'token' not in request.headers:
                return Response({"Error": "Token is required"}, status=400)
            try:
                user = Users.objects.get(auth_token=request.headers['token'])
            except:
                return Response({"Error": "Invalid Token"}, status=400)

            print(user.company.company_name, seller)
            if user.company.company_name != seller:
                return Response({"Error": "You are not authorized to update this invoice"}, status=400)

        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(InvoiceDetails.objects.filter(id=id).values('id', 'invoice_amount', 'seller', 'buyer', 'acknowledged', 'settled'))
