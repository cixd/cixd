from django.conf.urls import url
from django.shortcuts import redirect
from apps.news import views as news

urlpatterns = [
    url(r'^$', lambda x: redirect('/news/list/')),
    url(r'^list/$', news.list),
    url(r'^list/(?P<_id>.+)/$', news.detail),
]
