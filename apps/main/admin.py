from django.contrib import admin
from apps.main.models import *

class CoverImageAdmin(admin.ModelAdmin):
    list_display = ('order', 'title', 'date',)

admin.site.register(CoverImage, CoverImageAdmin)

# Admin page settings

from django.contrib.auth.models import User, Group

admin.site.site_header = 'CIxD Admin Page'
admin.site.site_title = 'CIxD Homepage Administration'
admin.site.unregister(User)
admin.site.unregister(Group)
