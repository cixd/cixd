from django.conf.urls import url
from apps.main import views as main

urlpatterns = [
    url(r'^$', main.index),
]
