# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from common.models import TimeStampedModel
from autoslug import AutoSlugField
from users.models import User


class Classroom(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    slug = AutoSlugField(populate_from='name', unique=True)
    is_busy = models.BooleanField(default=False, blank=True, verbose_name="Ocupado")
    location = models.CharField(max_length=70, verbose_name="Geoposición")
    current_user = models.ForeignKey(
        User,
        verbose_name="Usuario acual",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


