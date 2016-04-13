from django.conf.urls import url

from projects_helper.apps.students import views

urlpatterns = [
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^projects/$', views.ListProjects.as_view(), name="projects"),
    url(r'^projects/(?P<project_pk>\d+)/pick/$', views.pick_project, name="pick_project"),

]
