from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render

from projects_helper.apps.lecturers import email_check


@user_passes_test(email_check)
def profile(request):
    return render(request, "lecturers/profile.html")
