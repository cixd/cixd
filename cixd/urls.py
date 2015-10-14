from django.conf.urls import include, url
from django.contrib import admin

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # INCLUDE URL
    url(r'^$', include('apps.main.urls')),
    url(r'^about/', include('apps.about.urls')),
    url(r'^people/', include('apps.people.urls')),
    url(r'^news/', include('apps.news.urls')),
    url(r'^projects/', include('apps.projects.urls')),
    url(r'^publication/', include('apps.publication.urls')),

    # CKEDITOR
    url(r'^ckeditor/', include('ckeditor_uploader.urls')),

    # ADMIN
    url(r'^admin/', include(admin.site.urls)),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
