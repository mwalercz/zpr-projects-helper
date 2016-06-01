from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.forms import ModelForm

from projects_helper.apps.lecturers import is_lecturer
from projects_helper.apps.common.models import Project, Lecturer


@login_required
@user_passes_test(is_lecturer)
def profile(request):
    return render(request, "lecturers/profile.html")


class ListProjects(ListView, LoginRequiredMixin, UserPassesTestMixin):
    def test_func(self):
        return is_lecturer(self.request.user)

    model = Project
    template_name = "lecturers/project_list.html"
    context_object_name = 'projects'

    def get_context_data(self, **kwargs):
        # Call the base implementation first to get a context
        context = super(ListProjects, self).get_context_data(**kwargs)
        # Add in a QuerySet of all the books
        context['lecturer'] = Lecturer.objects.get(user=self.request.user)
        return context
    # def get_queryset(self):
    #     return Project.objects.filter(lecturer = Lecturer.objects.get(user = self.request.user))

@login_required
@user_passes_test(is_lecturer)
def project(request, project_pk):
    proj = Project.objects.get(pk=project_pk)
    return render(request, "lecturers/project_detail.html",
                  context={'project': proj})

@login_required
@user_passes_test(is_lecturer)
def project_delete(request, project_pk):
    proj =  Project.objects.get(pk=project_pk)
    if proj.lecturer.user == request.user:
        if proj.status() == 'free':
            proj.delete()
        else:
            messages.error(request, "Cannot delete occupied project")
    else:
        messages.error(request, "Cannot delete project: access denied")

    return redirect(reverse('lecturers:project_list'))


class ProjectForm(ModelForm):
    class Meta:
        model = Project
        fields = ['title', 'description']


@login_required
@user_passes_test(is_lecturer)
def project_new(request):
    form = ProjectForm(request.POST)
    if form.is_valid():
        proj = form.save(commit=False)
        proj.lecturer = Lecturer.objects.get(user = request.user)
        proj.save()
    return render(request, "lecturers/project_new.html",
                  context={'form': form})
