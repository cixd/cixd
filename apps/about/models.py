# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
import os

class Introduction(models.Model):
    content = models.TextField()

    class Meta:
        verbose_name = "Who we are"
        verbose_name_plural = "Who we are"

class Pursuit(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()

    class Meta:
        verbose_name = "What we pursue in research"
        verbose_name_plural = "What we pursue in research"

#class PursuitRelated(models.Model):
#    pursuit = models.ForeignKey(Pursuit, blank=True, null=True, related_name='rels')
#    title = models.CharField(max_length=200)
#    url = models.URLField(max_length=300)

class Offer(models.Model):
    content = models.TextField()

    class Meta:
        verbose_name = "Becoming CIxD members"
        verbose_name_plural = "Becoming CIxD members"

class Contact(models.Model):
    building = models.CharField(max_length=200, help_text="ex) #219, Dept. of Industrial Design, KAIST")
    address = models.CharField(max_length=200, help_text="ex) 291 Gwahangno, Yusong-gu, Daejeon 34141, Republic of Korea.")
    map_link = models.URLField(help_text="Google Map 링크")
    telephone = models.CharField(max_length=100)
    fax = models.CharField(max_length=100)

    class Meta:
        verbose_name = "Contact Us"
        verbose_name_plural = "Contact Us"
