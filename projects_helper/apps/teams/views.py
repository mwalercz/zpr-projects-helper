from django.core.urlresolvers import reverse_lazy
from vanilla import ListView, CreateView, DetailView, UpdateView, DeleteView
from .forms import TeamForm
from .models import Team


class TeamList(ListView):
    model = Team
    paginate_by = 20


class TeamCreate(CreateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy('teams:list')


class TeamDetail(DetailView):
    model = Team


class TeamUpdate(UpdateView):
    model = Team
    form_class = TeamForm
    success_url = reverse_lazy('teams:list')


class TeamDelete(DeleteView):
    model = Team
    success_url = reverse_lazy('teams:list')
