from django.shortcuts import render
from django.http import HttpResponse

import requests

def home(request):
    return render(request, 'home.html')

def devices(request):
    return HttpResponse("Listado de dispositivos")

API_BASE_URL = "https://65baj9nm87.execute-api.us-east-1.amazonaws.com/api"

def devices_list(request):
    """
    Obtiene la lista de dispositivos desde API Gateway
    """
    try:
        response = requests.get(f"{API_BASE_URL}/devices")
        devices = response.json().get("devices", [])
    except Exception as e:
        devices = []
    
    return render(request, "devices_list.html", {"devices": devices})

def device_detail(request, ap_mac):
    """
    Obtiene un dispositivo específico según su MAC Address
    """
    try:
        response = requests.get(f"{API_BASE_URL}/devices/{ap_mac}")
        device = response.json()
    except Exception as e:
        device = None
    
    return render(request, "device_detail.html", {"device": device})

