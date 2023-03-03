from django.urls import path
from passenger.views import * 


urlpatterns = [
    # path('pass/', include('passenger.urls')),
    path('',pass_home),
    path('form/',formsubmit),
    path('deletevalue/<int:id_value>', deletevalue),
    path('update/<int:id_value>', updatedata),
    path('dpassenger/<int:value>',deletepassenger),

]


#url types data url/<int:datavalue>   <str:strvalue> <slug:datavalue>  

