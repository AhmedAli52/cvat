# Copyright (C) CVAT.ai Corporation
#
# SPDX-License-Identifier: MIT

from collections import Counter

from django.db.models import Count
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import PermissionDenied
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from cvat.apps.engine.models import LabeledImage, LabeledShape, LabeledTrack, Task
from cvat.apps.engine.permissions import TaskPermission

ANNOTATION_MODELS = (LabeledShape, LabeledTrack, LabeledImage)


class AnnotationCountsView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request, task_id):
        task = get_object_or_404(Task.objects.select_related("organization"), pk=task_id)

        if not TaskPermission.create_scope_view(request, task).check_access().allow:
            raise PermissionDenied()

        counts = Counter()
        for model in ANNOTATION_MODELS:
            rows = (
                model.objects.filter(job__segment__task_id=task.id)
                .order_by()
                .values("label__name")
                .annotate(count=Count("id"))
            )
            for row in rows:
                counts[row["label__name"]] += row["count"]

        return Response(
            {
                "task_id": task.id,
                "total": sum(counts.values()),
                "classes": [
                    {"label": name, "count": count}
                    for name, count in sorted(counts.items(), key=lambda item: (-item[1], item[0]))
                ],
            }
        )
