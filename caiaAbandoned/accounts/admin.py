from django.contrib import admin

from caiaAbandoned.accounts.models import CaiaAbandonedUser


class UserAdmin(admin.ModelAdmin):
    list_display = ("email", "first_name", "last_name", "gender")


admin.site.register(CaiaAbandonedUser, UserAdmin)


