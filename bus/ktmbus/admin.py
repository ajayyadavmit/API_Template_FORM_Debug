from django.contrib import admin

from ktmbus.models import BusDB


class adminbusdb(admin.ModelAdmin):
    list_display = ('amount','name', 'location', 'city')
    list_editable = ('name',)
    search_fields = ('amount',)
    list_filter = ('amount',)

# Register your models here.

admin.site.register(BusDB,adminbusdb)
