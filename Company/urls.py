from django.urls import path
from .views import CompanyView, CompanyDetailView

urlpatterns = [
    path('companies/', CompanyView.as_view(), name='company'),
    path('companies/<int:id>/', CompanyDetailView.as_view(), name='company1'),
]
