from django.db import models
from django.template.defaultfilters import slugify

PROJECTS = [
    ('Residential building', 'Residential building'),
    ('Multifamily building', 'Multifamily building'),
    ('Co-working space', 'Co-working space'),
    ('Retail building', 'Retail building'),
    ('Industrial building', 'Industrial building'),
    ('Hotel', 'Hotel'),
    ('City garden', 'City garden'),
    ('Urban farm', 'Urban farm'),
    ('Non-Governmental Organisation', 'Non-Governmental Organisation')
]


class ProjectType(models.Model):
    type_of_project = models.CharField(max_length=40, choices=PROJECTS)

    def __str__(self):
        return self.type_of_project


class Project(models.Model):
    project_type = models.ForeignKey(to=ProjectType, on_delete=models.CASCADE)
    building_type_photo = models.URLField()
    description = models.TextField(max_length=300, blank=True, null=True)
    slug = models.SlugField(unique=True, editable=False)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.project_type}-{self.project_type_id}")
        return super().save(*args, **kwargs)

