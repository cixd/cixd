from django.contrib import admin
from apps.news.models import Article, Image
from ckeditor.widgets import CKEditorWidget as EditorWidget
from django import forms

class ImageInline(admin.TabularInline):
    model = Image
    extra = 1

class ArticleAdminForm(forms.ModelForm):
    content = forms.CharField(widget=EditorWidget())

    class Meta:
        model = Article
        fields = '__all__'

class ArticleAdmin(admin.ModelAdmin):
    form = ArticleAdminForm
    list_display = ('date', 'title',)
    inlines = [ImageInline,]

# Register Admins

admin.site.register(Article, ArticleAdmin)
