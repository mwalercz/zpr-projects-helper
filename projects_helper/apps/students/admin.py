from django.contrib import admin

# Register your models here.
from projects_helper.apps.students.models import Student

admin.site.register(Student)
