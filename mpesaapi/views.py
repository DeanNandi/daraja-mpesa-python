# mpesaapi/views.py
from django.http import HttpResponse
from .accessToken import get_mpesa_access_token

def get_access_token(request):
    access_token = get_mpesa_access_token()

    if access_token:
        return HttpResponse(f"Access Token: {access_token}")
    else:
        return HttpResponse("Failed to obtain access token.")
