# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2017-02-08 17:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classrooms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='classroom',
            name='is_busy',
            field=models.BooleanField(default=False, verbose_name='Ocupado'),
        ),
    ]