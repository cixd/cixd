# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
import os

class Member(models.Model):
    PHASE = [
        ("PROF", "Professor"),
        ("PHD", "Ph.D. Students"),
        ("M", "Master's Students"),
        ("PHDG", "Alumni - Ph.D."),
        ("MG", "Alumni - Master"),
    ]

    phase = models.CharField(max_length=4, choices=PHASE, help_text="현재 상태를 나타냅니다.")
    image = models.ImageField(upload_to='people', null=True, blank=True, help_text="프로필 사진")
    name_en = models.CharField(max_length=30)
    name_kr = models.CharField(max_length=30)
    email = models.EmailField()
    year = models.PositiveSmallIntegerField(default=2000, help_text="입학 년도 혹은 졸업 년도를 적어주세요.")
    current = models.CharField(max_length=100, help_text="현재 과정 혹은 직장을 적어주세요.", null=True, blank=True)

    class Meta:
        verbose_name = "Members or Alumni"
        verbose_name_plural = "Members or Alumni"

    def __str__(self):
        return '%s, %d' % (self.name_en, self.year)

class Degree(models.Model):
    member = models.ForeignKey(Member, related_name='degrees')
    year = models.PositiveSmallIntegerField(default=0, help_text="시작 년도를 적어주세요.")
    degree = models.CharField(max_length=20, help_text="Full 타이틀로 적어주세요. (ex. Ph.D., Illinois Institue of Technology, US)")
    department = models.CharField(max_length=100, help_text="학과", null=True, blank=True)
    university = models.CharField(max_length=100, help_text="학교", null=True, blank=True)

class Paper(models.Model):
    member = models.ForeignKey(Member, related_name='papers')
    title = models.CharField(max_length=200, help_text="졸업 논문의 전체 정보를 담아 적어주세요.")
    url = models.URLField()

    class Meta:
        verbose_name = "Graduation thesis"
        verbose_name_plural = "Graduation theses"
