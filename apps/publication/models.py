from django.db import models
from django.conf import settings
import os, datetime

class Publication(models.Model):
    PUBLISHTO = [
        ("JOUR", "Journal"),
        ("CONF", "Conference"),
    ]

    SCOPE = [
        ("INT", "International"),
        ("DOM", "Domestic"),
    ]

    publish_to = models.CharField(max_length=4, choices=PUBLISHTO)
    scope = models.CharField(max_length=3, choices=SCOPE)
    title = models.CharField(max_length=300)
    date = models.DateField(default=datetime.date.today)
    url = models.URLField()

    class Meta:
        verbose_name = "Journals & Conferences"
        verbose_name_plural = "Journals & Conferences"

    def __unicode__(self):
        return '%s' % (self.title)

class Other(models.Model):
    pass

class Award(models.Model):
    pass
