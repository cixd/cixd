# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
import os, datetime
from apps.people.models import Member

class Area(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "Area"
        verbose_name_plural = "Areas"

    def __unicode__(self):
        return '%s' % (self.title)

class Project(models.Model):
    area = models.ForeignKey(Area, related_name='projects')

    title = models.CharField(max_length=200)
    content = models.TextField(null=True, blank=True)
    thumbnail = models.ImageField(upload_to='projects', null=True, blank=True)
    start_year = models.CharField(max_length=10, default='2008')
    end_year = models.CharField(max_length=10, default='present')

    class Meta:
        verbose_name = "Project"
        verbose_name_plural = "Projects"

    def __unicode__(self):
        return '%s' % (self.title)

class Research(models.Model):
    project = models.ForeignKey(Project, related_name='researches')
    author = models.ForeignKey(Member, related_name='researches')

    title = models.CharField(max_length=200)
    paper = models.CharField(max_length=1000, help_text="FULL CITATION 형식으로 적어주세요.")
    url = models.URLField(help_text="논문 링크를 적어주세요.")
    date = models.DateField(default=datetime.date.today, help_text="Publication 날짜를 적어주세요.")
    abstract = models.TextField(null=True, blank=True, help_text="연구 논문의 abstract 혹은 연구의 요약 내용을 적어주세요.")
    funding = models.CharField(max_length=1000, null=True, blank=True)

    class Meta:
        verbose_name = "Research"
        verbose_name_plural = "Researches"

    def __unicode__(self):
        return '%s' % (self.title)

class Author(models.Model):
    research = models.ForeignKey(Research, related_name='co_authors')
    member = models.ForeignKey(Member, related_name='co_researches', null=True, blank=True)

    outlander = models.CharField(max_length=50, null=True, blank=True, help_text="저자가 연구실 외부인일 경우에는 member 란을 비우고, 이 곳에 이름을 적어주세요.")
    order = models.PositiveSmallIntegerField(default=2, help_text="1 저자를 제외한 2 저자부터 공동 저자의 순서를 정할 수 있습니다.")

class Image(models.Model):
    research = models.ForeignKey(Research, related_name="images")
    image = models.ImageField(upload_to='projects')
    caption = models.TextField(null=True, blank=True)

    def __unicode__(self):
        return '%s' % (self.image.url)

class Video(models.Model):
    research = models.ForeignKey(Research, related_name="videos")
    url = models.URLField()
    caption = models.TextField(null=True, blank=True)

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
        verbose_name = "Grant"
        verbose_name_plural = "Grants"

    def __unicode__(self):
        return '%s (%s)' % (self.title, self.sponsor_name)
