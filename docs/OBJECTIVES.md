# Objectives

Machine: Apple M1, 8 GB RAM, macOS 26.5 (25F71). CVAT commit: b52288c2b7f07184a0ddc6fb9b096ea7cebde9d4.

| ID | Field | Entry |
|---|---|---|
| MO-1 | What is measured | Response time of the per-class count endpoint for one task. |
| | How | `curl -w '%{time_total}'` against the local endpoint with a logged-in session, 5 runs, raw output saved. |
| | Target | Median of 5 runs at or below 300 ms (provisional until the first measurement). |
| | Conditions | Local Docker stack with linux/amd64 images under Rosetta, 500 images with COCO annotations, nothing else running, first request after a restart excluded. |
| | Not included | Video tasks, page render time, cold start. |

Why 300 ms: one grouped query should take tens of milliseconds natively. I allow several times that for emulation. A miss will be reported with its reason.
