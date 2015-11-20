# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
import os, datetime

class Category(models.Model):
    order = models.IntegerField(default=0, help_text="Publication 카테고리의 순서를 정해주세요. 숫자가 작을수록 위로 올라갑니다.")
    name = models.CharField(max_length=200, help_text="Publication 카테고리의 이름을 적어주세요.")

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"
        ordering = ['order', 'name']

    def __unicode__(self):
        return '%s' % (self.name)

class Publication(models.Model):
    SCOPE = [
        ("INT", "International"),
        ("DOM", "Domestic"),
    ]

    category = models.ForeignKey(Category, null=True, blank=True, related_name='publics')
    scope = models.CharField(max_length=3, choices=SCOPE)
    title = models.TextField()
    date = models.DateField(default=datetime.date.today)
    url = models.URLField(null=True, blank=True)

    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications"
        ordering = ['-date', 'title']

    def __unicode__(self):
        return '%s' % (self.title)

