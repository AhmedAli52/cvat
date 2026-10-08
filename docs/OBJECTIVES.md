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

## Results (MO-1)
Median 622 ms, min 599 ms, max 977 ms over 5 runs after one excluded warm-up request. Raw output: docs/evidence/mo1_runs.txt. Target of 300 ms: missed.

Method note: requests were made with curl and HTTP Basic auth, not a browser session as the table above says. Basic auth most likely adds password hashing to each request; I did not measure that separately. The stack ran linux/amd64 images under Rosetta on an Apple M1 with 8 GB RAM.

Baseline: the same 5-run curl against GET /api/users/self, an unrelated CVAT endpoint, gave a median of 713 ms (min 606, max 911); raw output in docs/evidence/baseline_runs.txt. It was no faster than the count endpoint, so the 300 ms target was most likely missed because of fixed per-request overhead (Basic auth, proxy, Rosetta emulation) and not the grouped query. The runs were made minutes apart and the spread is as large as the difference, so this is indicative, not exact. I did not time the query on its own.
