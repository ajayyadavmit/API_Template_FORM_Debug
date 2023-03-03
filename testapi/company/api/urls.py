
from django.urls import path, include
from api.views import *


from api.views import companyviewset
from rest_framework import routers

router = routers.DefaultRouter()

router.register(r'companies',companyviewset)


urlpatterns = [

    path("", home_api,  name='apihome'),
    path("cview/",cview.as_view(), name= "classbased"),
    path('v1/',include(router.urls)),

]






