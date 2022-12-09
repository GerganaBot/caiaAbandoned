from django.contrib import admin

from caiaAbandoned.accounts.models import CaiaAbandonedUser


class UserAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "gender")
    search_fields = ["email"]
    fields = [("first_name", "last_name"), ("username", "email"), "gender"]
    list_filter = ["gender"]


admin.site.register(CaiaAbandonedUser, UserAdmin)


