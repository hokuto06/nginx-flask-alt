from django.urls import path
from .views import *

urlpatterns = [
    path('', home),
    path('devices/', devices),
    path('app/', devices_list, name="devices_list"),
    path("app/<str:ap_mac>/", device_detail, name="device_detail"),
]
