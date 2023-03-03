from django.urls import path, include
from api.views import companyviewset
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'companies',companyviewset)

urlpatterns = [
    path('',include(router.urls)),
]


