from django.contrib import admin
from apps.people.models import Member, Degree, Paper

class DegreeInline(admin.TabularInline):
    model = Degree

class PaperInline(admin.TabularInline):
    model = Paper

class MemberAdmin(admin.ModelAdmin):
    list_display = ('year', 'name_en', 'email', 'phase',)
    inlines = [
        DegreeInline,
        PaperInline,
    ]

# Register Admins

admin.site.register(Member, MemberAdmin)
