# Plan

Start (acknowledgment): 20:22 PKT, 8 Oct 2026. Deadline: 04:22 PKT, 9 Oct 2026.
This plan was committed at 21:18 PKT. The first part of the window went on fork, clone, image pull and a slow dataset download (about 500 KB/s). No code had been written when this was committed.
Machine: Apple M1, 8 GB RAM, macOS 26.5 (25F71). CVAT commit: b52288c2b7f07184a0ddc6fb9b096ea7cebde9d4.
CVAT's prebuilt images are linux/amd64 and run emulated under Rosetta, so timings will be slower than native.

## Order and time budget (about 6 h 50 min remain)
| Step | Items | Time |
|---|---|---|
| Create task, import COCO annotations, see boxes in a job | setup | 20 min |
| Read models, permission classes, URL wiring, how the UI is built | K2 prep | 30 min |
| Django app `test`: count endpoint, CVAT login, task-level permission | 1, 5 | 60 min |
| Page, graph, empty state, failed-request state (includes getting the frontend to build) | 2, 3, 4 | 100 min |
| Speed target: 5 runs, raw output | 6 | 25 min |
| One grouping or filter | 7 | 20 min |
| Docs evidence, Loom | 10, docs | 45 min |
| Buffer | | 110 min |

## Decided to skip
Items 8 and 9 (WebSocket updates and reconnect). Items 1 to 4 are the floor and the machine has 8 GB of RAM. I will only reconsider if items 1 to 7 are done with evidence and at least 90 minutes remain.

## Decisions made up front
- Count in the database with one grouped query, not by loading annotations into Python.
- Backend in a new Django app named `test`, reusing CVAT's existing authentication and permission classes instead of writing my own.
- Dataset: 500 images from COCO val2017 (the first 500 by file name) with the official instances_val2017.json, chosen for 8 GB RAM.

## Risks
- The prebuilt Docker images do not contain a new `test` app. Mitigation: find CVAT's source-build or mount setup before writing code.
- Rebuilding the frontend may not fit in 8 GB of RAM. Mitigation: find the lightest way to build or run it before writing UI code.

## Branch note
The fork only had `develop`. I created `main` at the cloned commit b52288c2b7f07184a0ddc6fb9b096ea7cebde9d4 so the pull request can target `main` of my own fork, as the assessment requires.
