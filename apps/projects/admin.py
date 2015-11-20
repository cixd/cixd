from django.contrib import admin
from django.forms import BaseInlineFormSet
from apps.projects.models import *

class AreaAdmin(admin.ModelAdmin):
    list_display = ('title',)

class ProjectAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_year', 'end_year', 'area',)

class AuthorInline(admin.TabularInline):
    model = Author
    extra = 1
    ordering = ('order',)
    template = "admin/projects/research/edit_inline/tabular.html"

class ImageInline(admin.StackedInline):
    model = Image
    extra = 1

class VideoInline(admin.StackedInline):
    model = Video
    extra = 1

class ResearchAdmin(admin.ModelAdmin):
    list_display = ('title', 'date', 'project',)
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
