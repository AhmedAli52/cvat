# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from django.urls import path

from .views import AnnotationCountsPageView, AnnotationCountsView

urlpatterns = [
    path("annotation-counts/page", AnnotationCountsPageView.as_view()),
    path("tasks/<int:task_id>/annotation-counts", AnnotationCountsView.as_view()),
]
