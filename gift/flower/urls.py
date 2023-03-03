from django.urls import path
from flower.views import *


urlpatterns = [
    # path('flower/', flower_home),
    path('flower/', Flower_home_class.as_view(), name='orderflower'),
    path('flower-confirm/',flower_order, name='fconfirm'),
    path('delete-flower-order/<int:value>',deleteFlower, name='deleteOrder'),
    # path("",flower_home),
]

