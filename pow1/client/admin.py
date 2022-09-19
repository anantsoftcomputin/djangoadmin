from django.contrib import admin

# Register your models here.
from django.contrib import admin

from client.models import Address
from client.models import Client
from client.models import Reactor
from client.models import Plant
from client.models import Contact

# from client.models import Official_Address
# from client.models import Shipping_Address
# from client.models import PlantEntrance_Address


admin.site.register(Client)

admin.site.register(Reactor)


class PlantAdmin(admin.ModelAdmin):
    list_display = ('plant_location', 'plant_contact')
    search_fields = ['plant_location']


admin.site.register(Plant, PlantAdmin)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'title', 'company', 'phone_office', 'email')
    search_fields = ['first_name']


admin.site.register(Contact, ContactAdmin)


class AddressAdmin(admin.ModelAdmin):
    list_display = ('City', 'State', 'Country', 'Zipcode')
    search_fields = ['City']


admin.site.register(Address, AddressAdmin)

# admin.site.register(Official_Address)
# admin.site.register(Shipping_Address)
# admin.site.register(PlantEntrance_Address)