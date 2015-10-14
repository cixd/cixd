from django.conf.urls import url
from django.shortcuts import redirect
from apps.projects import views as projects

urlpatterns = [
    url(r'^$', projects.index),
    url(r'^project/(?P<name>.+)$', projects.project),
    url(r'^researchgrants/$', projects.grants),
]