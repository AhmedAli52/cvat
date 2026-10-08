# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from django.urls import path

from .views import AnnotationCountsView

urlpatterns = [
    path("tasks/<int:task_id>/annotation-counts", AnnotationCountsView.as_view()),
]
