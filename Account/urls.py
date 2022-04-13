from urllib.parse import urlparse
from django.urls import path
from .views import RegisterView, UserDetailView
urlpatterns = [
    path('users/', RegisterView.as_view(), name='users'),
    path('users/<int:id>/', UserDetailView.as_view(), name='users1'),
]
