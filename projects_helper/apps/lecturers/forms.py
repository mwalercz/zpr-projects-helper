from django.forms import ModelForm

from projects_helper.apps.common.models import Project


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']
        required_css_class = 'required'
