from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.TeamList.as_view(), name='list'),
    url(r'^new/$', views.TeamCreate.as_view(), name='create'),
    url(r'^(?P<pk>\d+)/$', views.TeamDetail.as_view(), name='detail'),
    url(r'^(?P<pk>\d+)/update/$', views.TeamUpdate.as_view(), name='update'),
    url(r'^(?P<pk>\d+)/delete/$', views.TeamDelete.as_view(), name='delete'),
]
