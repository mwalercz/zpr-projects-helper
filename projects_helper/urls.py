from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^projects/', include('projects_helper.apps.projects.urls', namespace='projects')),
]
