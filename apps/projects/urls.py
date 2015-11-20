from django.conf.urls import url
from django.shortcuts import redirect
from apps.projects import views as projects

urlpatterns = [
    url(r'^$', lambda x: redirect('/projects/list/')),
    url(r'^list/$', projects.index),
    url(r'^list/(?P<_id>.+)/$', projects.list),
    url(r'^grants/$', projects.grants),
]
