from django.conf.urls import url

from projects_helper.apps.students import views

urlpatterns = [
    url(r'^profile/$', views.profile, name="profile"),

]
