from django.contrib import admin
from apps.publication.models import Publication

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('publish_to', 'scope', 'title',)

admin.site.register(Publication, PublicationAdmin)
