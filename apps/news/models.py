# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
import os

from ckeditor.fields import RichTextField as EditorField

class Article(models.Model):
    date = models.DateField(help_text="이 날짜를 기준으로 뉴스가 정렬됩니다.")
    title = models.CharField(max_length=500)
    thumbnail = models.ImageField(upload_to='news', blank=True, null=True, help_text="썸네일 사이즈: 240x160px")
    content = EditorField()

    class Meta:
        ordering = ['-date', 'title']

class Image(models.Model):
    image = models.ImageField(upload_to='news')
    article = models.ForeignKey(Article, blank=True, null=True, related_name='images')

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(Image, self).delete(*args, **kwargs)
