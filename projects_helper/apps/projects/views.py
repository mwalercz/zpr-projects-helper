from django.core.urlresolvers import reverse_lazy
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import ProjectForm
from .models import Project


class ProjectList(ListView):
    model = Project
    paginate_by = 20


class ProjectCreate(CreateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('projects:list')


class ProjectDetail(DetailView):
    model = Project


class ProjectUpdate(UpdateView):
    model = Project
    form_class = ProjectForm
    success_url = reverse_lazy('projects:list')


class ProjectDelete(DeleteView):
    model = Project
    success_url = reverse_lazy('projects:list')
