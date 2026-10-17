# Methodology

This document describes the system behind *zero-to-path* — how topics are studied, verified, and tracked. It is public so that it can be examined, questioned, and adapted.

The material being studied is private. The method is not.

---

## 1. Knowledge maps

For each subject, exactly one file — the **knowledge map** — acts as the source of truth. Notes hold the material. The map holds what is done, what is verified, and what is at risk.

Each map collects, on a single page, the entire state of that subject:

- **Active source** — the one resource currently driving the subject.
- **Checklist of topics** — status, date confirmed, artifact, risks.
- **Practice register** — every drill, packet, and scenario, with its outcome.
- **Links to notes and practicums** — every note and every mentor-generated exercise tied to a topic.
- **Risk zones** — what is unclear, unresolved, or drifting.

A map without links to its notes is incomplete. A note that does not link back to its map does not count. Isolated notes are invisible to the system and get lost.

## 2. Four statuses

Every topic is in exactly one of four states:

| Status | Meaning |
|---|---|
| `not_started` | Not opened yet. |
| `in_progress` | Active work, not yet verified. |
| `notes_ready` | Notes exist, no proof of understanding yet. |
| `mastered` | Verified: clean recall + artifact + solved set of typical problems + written explanation. |

`mastered` is not a feeling. It is a claim backed by evidence. When evidence later fails — a mistake on review, on exam, on recall — the topic **returns to `in_progress`** and lands in the risk zone.

## 3. Mastery criteria

A topic earns `mastered` only when **all four** are true:

1. **Clean recall** — the answer, formula, code, or structure is reconstructed from memory, without prompts.
2. **Artifact** — a script, a scenario, a written sentence, a diagram: something exists outside the head.
3. **Solved set of typical problems** — not a single lucky run, but a series of representative tasks for the topic, all correct.
4. **Written explanation to the mentor** — the mechanism is described in the learner's own words, in writing, including the trap.

No note alone produces `mastered`. No single solved problem produces `mastered`. No "felt understood" produces `mastered`.

For language practice, the written explanation is complemented by **spoken repetition** — because pronunciation and rhythm cannot be verified on paper.

## 4. Supporting protocols

### Clean sheet

Before closing a unit, the work is repeated from scratch — no notes, no hints, no preview. If the structure does not return from memory, the unit is not closed.

### Error lab

Every unit includes at least one deliberate mistake — performed on purpose, diagnosed, and logged. The error is the lesson, not the obstacle.

### Spaced review

After a topic is mastered, it is revisited at fixed intervals — short, then longer, then longer again. A miss at any interval returns the topic to `in_progress`.

### Sequencing rule

A new unit starts only after the previous one has passed clean recall. Strictly enforced for practice-heavy subjects — languages and command-line training in particular. Skipping ahead accumulates unverified layers, and those layers collapse.

## 5. Drill register

Practical work is tracked by **drill IDs** — short codes for exercises, packets, and experiments. A drill is a unit of practice: it has a goal, an outcome, and a status.

A topic may be `in_progress` without drills. But it cannot be `mastered` without them. "Practiced in chat" is not practice. Practice has an artifact.

## 6. The AI mentor

The system is designed to be run **with an AI mentor** — not as an oracle, but as a structured counterpart.

The mentor operates under a **master config** — a versioned document, stored locally in the knowledge base, that defines the philosophy, phases, protocols, mastery criteria, exam formats, and interaction rules. The config is not fixed: it is revised regularly as the system learns what works, and every revision is preserved as history.

The mentor does four things:

1. **Generates practice.** Subject-specific scenarios, drills, and problem sets, tuned to the current level and tied to the active source.
2. **Checks results.** Reviews submitted solutions, identifies mistakes, and asks for corrections — without handing over final answers.
3. **Runs exams.** Periodically tests previously `mastered` topics; a mistake demotes the topic back to `in_progress`.
4. **Audits the system.** Verifies that notes and maps follow the standard, that `mastered` claims have evidence, and that no subject is silently drifting.

The relationship is deliberate: the mentor never writes the final solution. It asks questions, gives hints, and expects reconstruction. **The learner writes the code, solves the math, and explains their reasoning in writing to the mentor.** An AI that writes the solution for the learner breaks the entire system — because nothing is verified if nothing is reconstructed.

The mentor is expected to **notice drift before the learner does**: skipped days, imbalanced subjects, mastered claims without artifacts, notes not linked to maps. The mentor is the system's immune response — not its substitute.

## 7. The stack

Everything used in this project is **open, free, or both**. Nothing requires a paid licence, a subscription, or a proprietary account to reproduce.

- **Operating system** — Linux (Ubuntu).
- **Editor** — VS Code (open-source).
- **Knowledge base** — Obsidian (open-source, Markdown, plain text, portable).
- **Version control** — Git, with a public GitHub repository.
- **Language practice tools** — free / open vocabulary and audio trainers.
- **AI mentor** — open-weight or free-tier large language models.

The choice is not ideological. Free and open tools reduce friction, keep the material portable, and remove the excuse that cost is a barrier. If the path can only be walked by paying for it, it is not the path this project is testing.

## 8. Subject protocols

Each subject has a different shape — and a different way of being verified.

- **Mathematics.** Every formula must be derivable, not memorised. Every problem passes through: what is given → model → tool → solution → check → restatement. Mastery requires a written explanation of *why* the method works, not just a correct answer.
- **Computer Science.** Every concept is demonstrated by a mini-experiment that shows it running on the actual machine. Mastery requires reproducing the experiment from memory and predicting the output *before* running it.
- **Linux / command line.** Every scenario is performed in a sandbox. Every command's exit status is checked, not assumed. Mastery requires rebuilding the scenario from scratch, on a clean slate, with correct results and verified return codes.
- **Python.** Every solution is analysed at three levels: brute force, pattern / logic, pythonic. Mastery requires refactoring, line-by-line self-explanation, and comparison of approaches.
- **English.** Every unit covers form, meaning, usage, exceptions, and speech. Mastery requires clean recall of forms in writing **and** pronunciation of full sentences aloud.
- **Pet project.** Evolves across phases, adding a new layer each phase: pure logic → web service → systems-level performance. Each phase produces a public artifact.

## 9. Definition of done (per phase)

Phases are not passed by calendar. Each has explicit exit criteria — proven mastery in Python, Linux scenarios, mathematics, CS experiments, and English. A phase closes only when its criteria are met *and* demonstrated in front of the mentor or through a recorded self-examination.

## 10. Resource selection

One active source per subject at a time. It is replaced only when:

- The checklist of that source is fully `mastered`.
- At least two mini-exams on its topics have passed.

Before that, the source does not change — even if it gets boring. Switching mid-way is a hidden form of drift.

All sources are open, free, or widely accessible. Which sources to use is part of the path. Each learner finds their own.