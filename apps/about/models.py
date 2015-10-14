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
