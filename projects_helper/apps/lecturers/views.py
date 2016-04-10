from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

from projects_helper.apps.lecturers import is_lecturer


@user_passes_test(is_lecturer)
def profile(request):
    return render(request, "lecturers/profile.html")
