from django.contrib import admin

from caiaAbandoned.houses.models import House, Location


class HouseAdmin(admin.ModelAdmin):
    list_display = ("street", "street_number", "slug", "house_location", "description", "date_of_publication")


admin.site.register(House, HouseAdmin)
admin.site.register(Location)



