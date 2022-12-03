from django.contrib import admin

from caiaAbandoned.houses.models import House, Location


class HouseAdmin(admin.ModelAdmin):
    list_display = ("street", "street_number", "slug", "house_location", "description")


admin.site.register(House, HouseAdmin)
admin.site.register(Location)



