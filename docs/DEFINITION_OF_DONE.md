# Definition of Done

Each line points to a file under docs/evidence.

- [x] Stack runs and a job shows labelled boxes. Evidence: 3953 shapes from the API (docs/evidence/count_check_task1.txt). No screenshot of the boxes in a job was captured.
- [x] Endpoint returns correct counts, checked against a known task. Evidence: docs/evidence/count_check_task1.txt ("total 3953 | MATCH 78 78"), compared with counts derived from the COCO file (docs/evidence/expected_shape_counts.json). 78 classes because 2 of the 80 have no annotations in the 500 images.
- [x] Request without login is refused. Evidence: docs/evidence/auth_check.txt (HTTP 401).
- [x] User without access to the task is refused. Evidence: docs/evidence/auth_check.txt (HTTP 403 for a user with no access); also HTTP 404 for a missing task.
- [x] Page renders the graph. Evidence: docs/evidence/01-chart.png and docs/evidence/02-chart.png.
- [x] Empty state and failed-request state shown. Evidence: docs/evidence/05-empty.png, docs/evidence/03-not-logged-in.png, docs/evidence/04-no-access.png. The connection-failure branch was not exercised.
- [x] MO-1 measured 5 times, median and spread reported, raw output saved. Evidence: docs/evidence/mo1_runs.txt, median 622 ms, min 599, max 977.
- [x] Target met, or missed with the reason written down. Evidence: target 300 ms, missed (see OBJECTIVES.md).
- [ ] One extra filter or grouping. Not reached.
- [x] Everything not finished is listed. Not reached: item 7, items 8 and 9, a page inside cvat-ui. Known gaps: the endpoint reuses the task "view" permission and I did not read the OPA policy file; it replaces the default access-token enforcer with its own permission_classes; timing used Basic auth, not a session.
- [ ] Loom of 5 minutes or less answers K1 to K4. Evidence: link is in the submission email.
