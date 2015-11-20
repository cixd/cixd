from django.contrib import admin
from apps.about.models import *

class IntroductionAdmin(admin.ModelAdmin):
    list_display = ('id', 'content',)
    list_display_links = ('id', 'content',)

#class PursuitRelatedInline(admin.TabularInline):
#    model = PursuitRelated

class PursuitAdmin(admin.ModelAdmin):
    list_display = ('id', 'title',)
    list_display_links = ('id', 'title',)

#    inlines = [PursuitRelatedInline,]

class OfferAdmin(admin.ModelAdmin):
    list_display = ('id', 'content',)
    list_display_links = ('id', 'content',)

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'building', 'address',)
    list_display_links = ('id', 'building', 'address')

# Register Admins

admin.site.register(Introduction, IntroductionAdmin)
admin.site.register(Pursuit, PursuitAdmin)
admin.site.register(Offer, OfferAdmin)
admin.site.register(Contact, ContactAdmin)
