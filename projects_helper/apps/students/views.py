from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


# Create your views here.
from projects_helper.apps.students import email_check


@user_passes_test(email_check)
def profile(request):
    return render(request, "students/profile.html")



