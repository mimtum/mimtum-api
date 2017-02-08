# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.contrib import admin
from .models import Classroom


@admin.register(Classroom)
class ClassroomAdmin(admin.ModelAdmin):
    list_display = ('name', 'is_busy', 'current_user')
    search_fields = ['name', 'current_user__first_name', 'current_user__last_name']
