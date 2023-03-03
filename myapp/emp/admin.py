from django.contrib import admin
from emp.models import Employee, Testimonal

class adminemployee(admin.ModelAdmin):
    list_display = ('name','phone_no','location')
    list_filter= ('phone_no',)
    list_editable = ('phone_no',)
    search_fields = ('name',)

# Register your models here.
# Searching ofr model eamdi through search_Fields list_display list_filter list_editable tuples vaues to be given.add()
# in the html page, you need to give the url.py value that value would be mapped to functions call... 

admin.site.register(Employee,adminemployee)

admin.site.register(Testimonal)