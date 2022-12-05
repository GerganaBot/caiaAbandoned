from django import forms
from caiaAbandoned.projects.models import Project


class ProjectForm(forms.ModelForm):
    class Meta:
        model = Project
        fields = ['project_type', 'building_type_photo', 'description']
        widgets = {
            'project_type': forms.RadioSelect(),
            'building_type_photo': forms.TextInput(attrs={'placeholder': 'Link to image'}),
            'description': forms.Textarea(attrs={'placeholder': 'Description'}),
        }
        labels = {
            'building_type_photo': 'Photo'
        }


class ProjectDeleteForm(ProjectForm):
    def __int__(self, *args, **kwargs):
        super().__init__(self, *args, **kwargs)
        for (_, field) in self.fields.items():
            field.widget.attrs['disabled'] = 'disabled'
            field.widget.attrs['readonly'] = 'readonly'
