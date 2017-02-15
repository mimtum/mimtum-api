# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import serializers
from .models import Classroom


class ClassroomSerializer(serializers.ModelSerializer):

    class Meta:
        model = Classroom
        fields = ('id', 'name', 'slug', 'is_busy', 'location', 'current_user',
                  'modified')
        read_only_fields = ('id', 'slug', 'location',)



