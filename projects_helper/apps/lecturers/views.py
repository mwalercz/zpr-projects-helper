from django.contrib.auth.decorators import user_passes_test, login_required
from django.shortcuts import render, redirect, get_object_or_404
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.core.urlresolvers import reverse, reverse_lazy
from django.contrib import messages
from django.forms import ModelForm
from django.db import IntegrityError

from projects_helper.apps.lecturers import is_lecturer
from projects_helper.apps.common.models import Project, Lecturer
from projects_helper.apps.lecturers.forms import ProjectForm


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
                  context={'project': proj,
                           'lecturer': Lecturer.objects.get(user=request.user)})


@login_required
@user_passes_test(is_lecturer)
def project_delete(request):
    proj_pk = request.POST.get('to_delete', False)
    if proj_pk:
        proj = get_object_or_404(Project, pk=request.POST['to_delete'])
        if proj.lecturer.user == request.user:
            if proj.status() == 'free':
                 proj.delete()
            else:
                messages.error(request, "Cannot delete occupied project")
        else:
            messages.error(request, "Cannot delete project: access denied")

    return redirect(reverse('lecturers:project_list'))





@login_required
@user_passes_test(is_lecturer)
def project_new(request):
    if request.method == 'POST':
        form = ProjectForm(request.POST)
    else:
        form = ProjectForm()
    if form.is_valid():
        try:
            proj = form.save(commit=False)
            proj.lecturer = Lecturer.objects.get(user=request.user)
            proj.save()
        except IntegrityError as error:
            messages.error(request, "\n You must provide unique project name")
            return render(request, "lecturers/project_new.html",
                          context={'form': form})

        messages.info(request, "You have succesfully added new project: " + proj.title)
        return redirect(reverse('lecturers:project_list'))
    return render(request, "lecturers/project_new.html",
                  context={'form': form})


@login_required
@user_passes_test(is_lecturer)
def assign_team(request, project_pk):
    proj = Project.objects.get(pk=project_pk)
    if proj.lecturer.user == request.user:
        if proj.teams_with_preference().count() == 0:
            messages.error(request, "Cannot assign: No teams waiting for project")
        else:
            proj.assign_random_team()
    else:
        messages.error(request, "Cannot assign: access denied")

    return redirect(reverse_lazy('lecturers:project', kwargs={'project_pk': proj.pk}))

@login_required
@user_passes_test(is_lecturer)
def modify_project(request, project_pk):
    proj = get_object_or_404(Project, pk=project_pk)
    form = ProjectForm(request.POST or None, instance=proj)
    if form.is_valid():
        form.save()
        messages.info(request, "You have succesfully updated project:" + proj.title)
        return redirect(reverse("lecturers:project", kwargs={'project_pk': proj.pk}))
    return render(request, "lecturers/project_modify.html",
                  context={'form': form,
                           'project': proj})
