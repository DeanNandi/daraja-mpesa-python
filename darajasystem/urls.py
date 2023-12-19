# darajasystem/urls.py
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mpesa/', include('mpesaapi.urls')),
    # Add more URL patterns as needed
]

