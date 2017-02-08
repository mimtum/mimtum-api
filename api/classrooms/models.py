# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from common.models import TimeStampedModel
from autoslug import AutoSlugField
from location_field.models.plain import PlainLocationField
from users.models import User


class Classroom(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    slug = AutoSlugField(populate_from='name', unique=True)
    is_busy = models.BooleanField(default=False, blank=True, verbose_name="Ocupado")
    city = models.CharField(
        max_length=255,
        default="Santa Marta, Magdalena",
        verbose_name="Ciudad",
        blank=True
    )
    location = PlainLocationField(
        based_fields=['city'],
        zoom=7
    )
    current_user = models.ForeignKey(
        User,
        verbose_name="Usuario acual",
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


