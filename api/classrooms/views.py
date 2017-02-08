# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, mixins
from .serializers import ClassroomSerializer
from .models import Classroom


class ClassroomViewSet(mixins.ListModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    """
    list and Update classrooms
    """
    queryset = Classroom.objects.filter()
    serializer_class = ClassroomSerializer
    permission_classes = (AllowAny,)
    filter_fields = ('is_busy',)

    def list(self, request, *args, **kwargs):
        self.permission_classes = (AllowAny,)
        return super(ClassroomViewSet, self).list(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        self.permission_classes = (IsAuthenticated,)
        return super(ClassroomViewSet, self).update(request, *args, **kwargs)

