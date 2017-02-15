# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from rest_framework import permissions


class ClassroomPermission(permissions.BasePermission):

    def has_permission(self, request, view):
        if view.action == 'list':
            return True
        if view.action in ['update', 'partial_update']:
            return request.user.is_authenticated()
        else:
            return False

    def has_object_permission(self, request, view, obj):
        if view.action in ['update', 'partial_update']:
            return request.user.is_authenticated()
        else:
            return False
