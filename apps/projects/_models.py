# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
import os, datetime
from apps.people.models import Member

class Area(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "01 Research area (FIRST LEVEL)"
        verbose_name_plural = "01 Research areas (FIRST LEVEL)"

    def __unicode__(self):
        return '%s' % (self.title)

class Category(models.Model):
    group = models.ForeignKey(Area, related_name='categories', null=True, blank=True)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "02 Category (SECOND LEVEL)"
        verbose_name_plural = "02 Categories (SECOND LEVEL)"

    def __unicode__(self):
        return '%s' % (self.title)

class Project(models.Model):
    category = models.ForeignKey(Category, related_name='projects')
    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    begin_year = models.CharField(max_length=10, default='0000')
    end_year = models.CharField(max_length=10, default='present')

    class Meta:
        verbose_name = "03 Project (THIRD LEVEL)"
        verbose_name_plural = "03 Projects (THIRD LEVEL)"

    def __unicode__(self):
        return '%s' % (self.title)

class Thesis(models.Model):
    project = models.ForeignKey(Project, related_name='theses')
    title = models.CharField(max_length=500)
    abstract = models.TextField(null=True, blank=True)
    url = models.URLField()
    author = models.ForeignKey(Member, related_name='theses')
    date = models.DateField(default=datetime.date.today)

    class Meta:
        verbose_name = "Publication"
        verbose_name_plural = "Publications"

    def __unicode__(self):
        return '%s' % (self.title)

class Author(models.Model):
    thesis = models.ForeignKey(Thesis, related_name='co_authors')
    member = models.ForeignKey(Member, related_name='co_theses', null=True, blank=True)
    outlander = models.CharField(max_length=50, null=True, blank=True, help_text="저자가 연구실 외부인일 경우에는 member 란을 비우고, 이 곳에 이름을 적어주세요.")
    order = models.PositiveSmallIntegerField(default=2, help_text="1 저자를 제외한 2 저자부터 공동 저자의 순서를 정할 수 있습니다.")

class Grant(models.Model):
    SPONSOR = [
        ("GOV", "Government / KAIST sponsored"),
        ("COR", "Corporation sponsored"),
    ]

    sponsor = models.CharField(max_length=3, choices=SPONSOR)
    sponsor_name = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    start_year = models.CharField(max_length=10, default='0000')
    end_year = models.CharField(max_length=10, default='present')
    url = models.URLField(null=True, blank=True)
    open_date = models.DateField(default=datetime.date.today, help_text="이 날짜 포함, 그 이후로 공개가 됩니다.")

    class Meta:
        verbose_name = "Research Grant"
        verbose_name_plural = "Research Grants"

    def __unicode__(self):
        return '%s (%s)' % (self.title, self.sponsor_name)
