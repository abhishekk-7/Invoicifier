from django.urls import path
from .views import InvoiceDetailView, InvoiceView

urlpatterns = [
    path('invoices/', InvoiceView.as_view(), name='invoice'),
    path('invoices/<int:id>/', InvoiceDetailView.as_view(), name='invoice-detail'),
]
