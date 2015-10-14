from django.conf.urls import url
from django.shortcuts import redirect
from apps.people import views as people

urlpatterns = [
    url(r'^$', lambda x: redirect('/people/members/')),
    url(r'^members/$', people.members),
    url(r'^members/[A-Z]+$', people.member),
    url(r'^alumni/$', people.alumni),
]
