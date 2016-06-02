from django.conf.urls import url

from projects_helper.apps.students import views

urlpatterns = [
    url(r'^profile/$', views.profile, name="profile"),
    url(r'^teams/$', views.ListTeams.as_view(), name="team_list"),
    url(r'^teams/new/$', views.new_team, name="new_team"),
    url(r'^teams/(?P<team_pk>\d+)/join$', views.join_team, name="join_team"),
    url(r'^projects/$', views.ListProjects.as_view(), name="project_list"),
    url(r'^projects/(?P<project_pk>\d+)/$', views.project, name="project"),
    url(r'^projects/(?P<project_pk>\d+)/pick/$', views.pick_project, name="pick_project"),

]
