from django.contrib import admin
from apps.publication.models import Category, Publication

class CategoryAdmin(admin.ModelAdmin):
    list_display = ('order', 'name',)

class PublicationAdmin(admin.ModelAdmin):
    list_display = ('scope', 'title',)

admin.site.register(Category, CategoryAdmin)
admin.site.register(Publication, PublicationAdmin)
