# zero-to-path

> This is a personal experiment: can a person starting from zero become an engineer through small, consistent steps?

[![License: MIT](https://img.shields.io/badge/License-MIT-blue?style=flat-square)](LICENSE)
[![Status](https://img.shields.io/badge/status-phase%200-brightgreen?style=flat-square)](#roadmap)
[![Last Updated](https://img.shields.io/badge/updated-2026--10--17-lightgrey?style=flat-square)](#current-progress)

---

## What this is

A public record of a long-term, self-directed engineering education — documented as a reproducible system rather than a diary.

The method is open. The journey is tracked.

The goal is to build a career from backend development into AI infrastructure, on a foundation of mathematics, computer science, Linux, and English. Not by heroic sprints, but by small, consistent steps measured over years.

## Why publish

If small steps work, this repository will show it. If they don't, it will show that too. Either outcome is worth documenting.

## How it works

Three pillars:

- **Knowledge maps** — one per subject. The single source of truth for topic status, and the hub that collects every note, drill, scenario, and practicum.
- **Mastery criteria** — a topic is only "mastered" after clean recall, a hands-on artifact, a solved set of typical problems, and a written explanation to the AI mentor.
- **Supporting discipline** — clean-sheet repetition, deliberate error labs, and spaced review at fixed intervals.

Full breakdown → [METHODOLOGY.md](METHODOLOGY.md)
Founding philosophy → [PHILOSOPHY.md](PHILOSOPHY.md)

---

## Roadmap

Four phases. The timeline is defined by mastery, not by calendar.

| Phase | Goal | Core stack | Status |
|---|---|---|---|
| **0 — Foundation** | Base in math, CS, language; first code | Python (basics), Linux CLI, school-level algebra, CS fundamentals, English A1→B1 | **← current** |
| **1 — Backend** | Junior Backend Developer | Python (OOP, FastAPI), PostgreSQL, SQL, Docker, REST | pending |
| **2 — Systems** | Professional backend, first C++ | C++ (memory, STL), linear algebra | pending |
| **3 — AI Infrastructure** | Engineer for AI systems | C++ (concurrency), CUDA/OpenCL, GPU architecture, pybind11 | pending |

---

## Current Progress

*Last updated: 2026-10-17*

### Python — Stepik course (389 / 2438)
- **Current topic:** 4.3 — nested and cascaded conditions (`elif`).
- **Active drill:** `PY-D01` — branch classifier, level 0 in progress.
- **Open debt:** L1 mini-exam (`PY-E01`) not yet taken.

### Mathematics — Algebra 7 (Mordkovich)
- **Current topic:** §5 tail — percentages and mixtures.
- **Active drill:** `M-DRILL-alloys` — 2 clean solutions passed.
- **Open debt:** written explanation of the `m_removed = 0` trap not yet delivered.

### Linux / Bash — Shotts + playground scenarios
- **Current unit:** Unit 2 — file operations and wildcards.
- **Active drill:** `L-DRILL-U2` — tasks 1–6 submitted; tasks 7–8 pending.
- **Open debt:** Error Lab and clean repeat not yet passed.

### Computer Science — Informatics 6 (Bosova, 100 / 215)
- **Current topic:** §14 — introduction to algorithms.
- **Active drill:** `CS-E01` — express `mkdir -p` as a flowchart and as a verbal algorithm. Not started.

### English — grammar (Murphy) + practice (English File)
- **Grammar:** Unit 5 (Present Simple Affirmative) — `mastered` (2026-10-15).
- **Practice:** Unit 2B (Wh-/How-questions with `be`) — in progress.
- **Open debt:** `EN-PACKET-2B` (5 sentences) not yet submitted.

### Pet project — `expense_tracker` (CLI)
- **Status:** not started. Structure will mirror Linux Unit 1 (`src/`, `data/`, nested directories).

*Full topic-level detail lives in the knowledge maps.*

---

## Repository structure

```text
zero-to-path/  
├── README.md # the showcase  
├── PHILOSOPHY.md # why this path — the manifest  
├── METHODOLOGY.md # how the system works  
├── LICENSE  
├── .gitignore # keeps private material out of the repository  
├── .gitattributes # encoding and line-ending safety  
├── code/ # public code samples worth revisiting years later  
├── templates/ # knowledge map, daily log, drill templates  
└── docs/ # optional additional documentation
```

Study notes are maintained in **Obsidian** (open-source, plain-text Markdown). Code is written in **VS Code** (open-source). Both run on Linux.

---

## Tooling

- **OS:** Linux (Ubuntu)
- **Editor:** VS Code
- **Knowledge base:** Obsidian
- **Version control:** Git + GitHub
- **AI mentor:** open-weight or free-tier large language models

All tools are open-source, free, or both. Nothing requires a paid licence to reproduce.

---

## License

[MIT](LICENSE)