# mpesaapi/urls.py
from django.urls import path
from .views import get_access_token

urlpatterns = [
    path('get-access-token/', get_access_token, name='get_access_token'),
    # Add more URL patterns as needed
]
