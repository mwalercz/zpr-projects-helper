from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'', include('projects_helper.apps.common.urls', namespace='common')),
    url(r'^projects/', include('projects_helper.apps.projects.urls', namespace='projects')),
    url(r'^students/', include('projects_helper.apps.students.urls', namespace='students')),
    url(r'^lecturers/', include('projects_helper.apps.lecturers.urls', namespace='lecturers')),
    url(r'^accounts/', include('registration.backends.simple.urls', namespace='accounts')),

]
