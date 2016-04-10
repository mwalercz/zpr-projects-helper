from django.contrib.auth.decorators import user_passes_test
from django.shortcuts import render


# Create your views here.
from projects_helper.apps.students import is_student


@user_passes_test(is_student)
def profile(request):
    return render(request, "students/profile.html")



