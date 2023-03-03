from django.contrib import admin

# Register your models here.
from app.models import Student, newstudent, Place, Restaurant

# admin.site.register( Student)

c = (Student, newstudent, Place, Restaurant)

for m in c: 
    admin.site.register(m)