# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import viewsets, mixins
from .serializers import ClassroomSerializer
from .permissions import ClassroomPermission
from .models import Classroom


class ClassroomViewSet(mixins.ListModelMixin,
                       mixins.UpdateModelMixin,
                       viewsets.GenericViewSet):
    """
    list and Update classrooms
    """
    queryset = Classroom.objects.filter()
    serializer_class = ClassroomSerializer
    permission_classes = (ClassroomPermission,)
    filter_fields = ('is_busy',)

    def perform_update(self, serializer):
        if self.request.data['is_busy'] == 'true':
            serializer.save(current_user=self.request.user)
        else:
            serializer.save(current_user=None)


