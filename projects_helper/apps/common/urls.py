from django.conf.urls import url, include

from projects_helper.apps.common import views

urlpatterns = [
    url(r'^login/$', views.user_login, name="login"),
]
