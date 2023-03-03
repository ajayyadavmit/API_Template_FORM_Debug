from django.contrib import admin
from django.urls import path
from emp.views import *

urlpatterns = [
    
    path("home/",emp_home),
    path("add-emp/",add_emp),
    path('delete-emp/<int:emp_id>',delete_emp),
    path('update-emp/<int:emp_id>',update_emp),
    path('testimonals/',emp_testimonals),
    path('feedback/',emp_feedback),
]
