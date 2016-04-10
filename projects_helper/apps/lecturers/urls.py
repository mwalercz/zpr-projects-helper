from django.conf.urls import url

from projects_helper.apps.lecturers import views

urlpatterns = [
    url(r'^profile/$', views.profile, name="profile"),

]
