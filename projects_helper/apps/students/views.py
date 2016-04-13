from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse
from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView

from projects_helper.apps.common.models import Project, Team, Student
from projects_helper.apps.students import is_student


@login_required
@user_passes_test(is_student)
def profile(request):
    return render(request,
                  "students/profile.html",
                  {'user': request.user})


class ListProjects(ListView, LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return is_student(self.request.user)

    model = Project
    template_name = "students/projects.html"
    context_object_name = 'projects'


@login_required
@user_passes_test(is_student)
def pick_project(request, project_pk):
    student = Student.objects.get(user=request.user)
    team = student.team
    team.project_preference = Project.objects.get(pk=project_pk)
    team.save()
    return redirect(reverse('students:projects'))
