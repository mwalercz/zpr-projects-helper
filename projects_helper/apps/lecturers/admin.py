from django.contrib import admin

# Register your models here.
from projects_helper.apps.lecturers.models import Lecturer

admin.site.register(Lecturer)
