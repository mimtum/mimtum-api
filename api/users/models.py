# -*- coding: utf-8 -*-
from __future__ import unicode_literals, absolute_import

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.encoding import python_2_unicode_compatible
from common.models import TimeStampedModel


FACULTIES = (
    ('ING','Ingenieria'),
    ('SALUD','Salud'),
    ('ECO','Ciencias economicas y empesariales'),
    ('HUM','Ciencias humanas'),
    ('BAS','Ciencias basicas')
)

class Subject(TimeStampedModel):
    name = models.CharField(max_length=255, verbose_name="Nombre")
    faculty = models.CharField(
        max_length=25,
        choices=FACULTIES,
        verbose_name="Facultad",
        blank=True
    )

    def __str__(self):
        return self.name


@python_2_unicode_compatible
class User(AbstractUser):
    subjects = models.ManyToManyField(
        Subject,
        verbose_name="Asignaturas",
        blank=True
    )

    def __str__(self):
        return self.username



