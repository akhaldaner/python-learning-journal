# Python Learning Journal

**Daily progress tracker for learning computer science, Python, mathematics, Linux, and English.**

[![GitHub](https://img.shields.io/badge/GitHub-akhaldaner-181717?style=for-the-badge&logo=github)](https://github.com/akhaldaner)
[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python)](https://python.org)
[![Linux](https://img.shields.io/badge/Linux-Ubuntu-E95420?style=for-the-badge&logo=ubuntu)](https://ubuntu.com)
[![Obsidian](https://img.shields.io/badge/Obsidian-1.7.6-7C3AED?style=for-the-badge&logo=obsidian)](https://obsidian.md)
[![License](https://img.shields.io/badge/License-MIT-blue?style=for-the-badge)](LICENSE)

---

## Table of Contents

- [Description](#description)
- [Project Structure](#project_structure)
- [Installation](#installation)
- [Usage](#usage)
- [Current Progress](#current_progress)
- [License](#license)

---

## Description

This repository serves as my personal learning diary. It tracks my progress across five core areas:
- **Python** — syntax, functions, OOP, and backend development.
- **Mathematics** — algebra, mathematical analysis, linear algebra.
- **Linux** — command-line proficiency, system administration.
- **English** — vocabulary, grammar, and technical communication.
- **Computer Science** — architecture, algorithms, data structures.

All study notes are maintained in **Obsidian** (vault: `free_in_the_knowledge/`) and synchronised with this Git repository. Daily logs and knowledge maps (`_map_of_content`) are kept in Markdown for easy navigation and version control.
The goal is to reach **Junior Python Backend Developer** level within 2–2.5 years, while building a portfolio of projects and maintaining a consistent learning habit.

---

## Project_structure

The repository is structured around an Obsidian vault (`free_in_the_knowledge/`) synchronised with Git. Each subject folder contains a `_map_of_content.md` file that serves as a navigation hub for that topic.

```text
free_in_the_knowledge/  
├── CS/  
│ ├── CS_map_of_content.md  
│ └── Notes/  
├── Daily/  
│ ├── Logs/ # Daily progress reports  
│ └── Templates/ # Note and report templates  
├── English/  
│ ├── English_File/  
│ │ └── Notes/  
│ ├── English_map_of_content.md  
│ ├── Murphy_Grammar_in_Use/  
│ │ └── Notes/  
│ └── Vocabulary/  
├── GitHub/  
│ ├── Notes/  
│ └── python-learning-journal/ # This repository  
├── Inbox/ # Temporary notes and ideas  
├── Linux/  
│ ├── Commands-Cheatsheet.md  
│ ├── Linux_map_of_content.md  
│ └── Notes/  
├── Math/  
│ ├── Formulas.md  
│ ├── Math_map_of_content.md  
│ ├── Notes/  
│ └── Tasks/  
├── Projects/ # First project (future)  
└── Python/  
├── Notes/  
├── Python_map_of_content.md  
└── Tasks/
```

---

## Installation

1. Clone the repository:

  ```bash
git clone https://github.com/akhaldaner/python-learning-journal.git
cd python-learning-journal
  ```

2. Open the vault in Obsidian (optional):
- Open Obsidian.
- Click "Open folder as vault" and select the `free_in_the_knowledge/` folder inside the cloned repository.

3. Ensure Python 3.12+ is installed (to run code examples):

```bash
python3 --version
```

If not installed, use your system package manager (e.g., `sudo apt install python3` on Ubuntu).

No additional dependencies are required — all notes are in plain Markdown.

---

## Usage

### Viewing Notes

Open the Obsidian vault:

1. Launch Obsidian.
2. Click **"Open folder as vault"**.
3. Select the `free_in_the_knowledge/` folder from the cloned repository.

Once opened, use the knowledge maps (`*_map_of_content.md`) as entry points:

- `Python/Python_map_of_content.md` — current Python topics and progress.
- `Math/Math_map_of_content.md` — algebra, geometry, formulas.
- `Linux/Linux_map_of_content.md` — command-line cheatsheets.
- `English/English_map_of_content.md` — grammar and vocabulary.
- `CS/CS_map_of_content.md` — computer science and architecture.

### Running Code Examples

Navigate to the Python folder and execute scripts:

```bash
cd Python/Tasks/
python3 min_of_four.py
```

### Daily Logging

New daily reports are created using the template in Daily/Templates/daily_log.md. Place them in Daily/Logs/YYYY/MM/ with the format DD.md.

Example:

```bash
cp Daily/Templates/daily_log.md Daily/Logs/2026/09/05.md
```

Then fill in the sections for sleep, sport, studies, and reflections.

---

## Current_Progress

*Last updated: 2026-09-09*

| Subject              | Progress                                                                                                                             | Status      |
| :------------------- | :----------------------------------------------------------------------------------------------------------------------------------- | :---------- |
| **Python**           | Logical operators (`and`, `or`, `not`)                                                                                               | In progress |
| **Mathematics**      | Grade 7, Chapter 1, § 1. Numerical and algebraic expressions. § 2. What mathematical language is. § 3. What a mathematical model is. | In progress |
| **Linux**            | Stepik ~41                                                                                                                           | In progress |
| **English**          | English File 4e Beginner (Episode 1)<br>English File 4e Workbook (Episode 1)<br>Murphy Essential Grammar in Use Elementary (Unit 2)  | In progress |
| **Computer Science** | Binary arithmetic, Boolean logic                                                                                                     | In progress |

**Daily routine:**  
- Learning sessions: 6–8 hours on home days, 3–4 hours on office days.  
- Anki/ReWord: 20 new words + ~400 repetitions daily.  
- Regular commits to GitHub.  
- Physical exercise, walks, and playing music incorporated into the daily routine.


---

## License

This project is licensed under the [MIT](LICENSE).

**Author:** [akhaldaner](https://github.com/akhaldaner)

---
