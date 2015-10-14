from django.contrib import admin
from apps.projects.models import *

class AreaAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_year', 'end_year', 'area',)

class AuthorInline(admin.TabularInline):
    model = Author

class ImageInline(admin.TabularInline):
    model = Image

class VideoInline(admin.TabularInline):
    model = Video

class ResearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'author', 'project',)
    inlines = [
        AuthorInline,
        ImageInline,
        VideoInline,
    ]

class GrantAdmin(admin.ModelAdmin):
    list_display = ('title', 'sponsor_name',)

# Register Admins

admin.site.register(Area, AreaAdmin)
admin.site.register(Project, ProjectAdmin)
admin.site.register(Research, ResearchAdmin)
admin.site.register(Grant, GrantAdmin)
