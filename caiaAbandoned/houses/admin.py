from django.contrib import admin

from caiaAbandoned.houses.models import House, Location


class HouseAdmin(admin.ModelAdmin):
    list_display = ("zone_name", "street", "street_number", "slug", "house_location", "description", "date_of_publication")
    list_filter = ["date_of_publication", "zone_name", "street"]
    search_fields = ["street"]


admin.site.register(House, HouseAdmin)
admin.site.register(Location)



