from django.contrib import admin
from django.urls import path
from ktmbus.views import *

urlpatterns = [
    path('',busview),
    path('localbus/',localbus),
    path('mainbus/',mainbus),
]
