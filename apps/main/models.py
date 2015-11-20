# -*- coding: utf-8 -*-

from django.db import models
from django.conf import settings
import os

class CoverImage(models.Model):
    order = models.IntegerField(default=0, help_text="이 값의 순서로 정렬 후, 날짜 정렬이 됩니다.")
    title = models.CharField(max_length=200, null=True, blank=True)
    date = models.DateField(help_text="사진 위에 날짜가 함께 표시됩니다.")
    image = models.ImageField(upload_to='main', help_text="사이즈: 770px X 400px")

    class Meta:
        verbose_name = "CIxD Photo booth"
        verbose_name_plural = "CIxD Photo booth"

    def delete(self, *args, **kwargs):
        self.image.delete()
        super(CoverImage, self).delete(*args, **kwargs)
