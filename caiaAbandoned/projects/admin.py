from django.contrib import admin

from caiaAbandoned.projects.models import Project, ProjectType


class ProjectAdmin(admin.ModelAdmin):
    list_display = ("project_type", "slug", "description", "user", "house")
    search_fields = ["slug"]
    list_filter = ["project_type"]


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectType)

