from django.contrib import admin
from mobile.models import Phone
# Register your models here.


class displayPhone(admin.ModelAdmin):
    list_display = ('name','cost')
    list_editable = ('cost',)
    list_filter = ('cost',)
    search_fields = ('name',)

admin.site.register(Phone, displayPhone)