from django.contrib import admin

from caiaAbandoned.houses.models import House, Location


class HouseAdmin(admin.ModelAdmin):
    list_display = ("street", "slug")


admin.site.register(House, HouseAdmin)
admin.site.register(Location)


