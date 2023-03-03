from django.contrib import admin
from passenger.models import * 
# Register your models here.

class PassengerDetailsAdmin(admin.ModelAdmin):
    list_display = ('name','caste','comments','child_no')
    list_editable = ('child_no','caste')
    search_fields = ('name','caste')
    list_filter = ('child_no',)

admin.site.register(PassengerDetails, PassengerDetailsAdmin)