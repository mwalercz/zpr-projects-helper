from django.conf.urls import url

from projects_helper.apps.lecturers import views

urlpatterns = [
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^projects/$', views.ListProjects.as_view(), name="project_list"),
    url(r'^projects/(?P<project_pk>\d+)/$', views.project, name="project"),
    url(r'^projects/del/$', views.project_delete, name="project_delete"),
    url(r'^projects/(?P<project_pk>\d+)/assign/$', views.assign_team, name="assign_team"),
    url(r'^projects/new/$', views.project_new, name="project_new"),

]
