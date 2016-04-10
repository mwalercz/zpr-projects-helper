from django.conf.urls import url

from projects_helper.apps.common import views

urlpatterns = [
    url(r'^login/$', views.user_login, name="login"),

]
