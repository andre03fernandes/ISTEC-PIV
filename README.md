# ISTEC-PIV

> **Programming IV** · Computer Engineering (LEI) · ISTEC · 2026  
> Instructor: Miguel Rodrigues

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Git](https://img.shields.io/badge/VCS-Git-orange?logo=git&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-green)

---

## About

This repository contains all exercises, notes, and course materials developed throughout the **Programming IV** discipline at ISTEC.  
The course covers Python fundamentals, version control with Git, Markdown documentation, object-oriented programming, and a final project.

**Grade formula:** `Final Grade = Exam × (15/20) + Project × (5/20)`

---

## Progress

| # | Session | Topics | Status |
|---|---------|--------|--------|
| 1–2 | Environment & VCS | Python setup, Git, GitHub, IDEs | ✅ Done |
| 3–4 | Git + Python Intro | Git commands, Markdown, variables, data types | ✅ Done |

### Task List

- [x] Environment setup (Python 3.x + VS Code)
- [x] Git repository initialized and linked to remote
- [x] Basic Git commands (`clone`, `commit`, `push`, `pull`, `branch`, `merge`)
- [x] Markdown documentation (this README)
- [x] Python comments and docstrings
- [x] Variables and naming conventions (camelCase, PascalCase, snake_case)
- [x] Python data types (int, float, str, bool, list, tuple, dict, set)
- [x] Compound data structures (Exercise 1)
- [ ] Control flow (if / elif / else, ternary operator)
- [ ] Loops (`for`, `while`, `break`, `continue`)
- [ ] Functions and scope
- [ ] Object-Oriented Programming (classes, inheritance, polymorphism)
- [ ] Final project

---

## Repository Structure

```
ISTEC-PIV/
├── Content/                  # Lecture slides (PDF)
│   ├── sessao-1_2-nosp.pdf   # Sessions 1 & 2 — Intro, VCS, IDEs
│   └── sessao-3_4.pdf        # Sessions 3 & 4 — Git, Markdown, Python basics
├── Exercises/                # Practical exercises
│   └── exercicio1.py         # Compound data structures
└── README.md
```

---

## Prerequisites

- [Python 3.x](https://www.python.org/downloads/)
- [Git](https://git-scm.com/)
- [Visual Studio Code](https://code.visualstudio.com/)

---

## How to Run

Clone the repository and run any exercise from the project root:

```bash
git clone <your-repo-url>
cd ISTEC-PIV
```

**Exercise 1 — Compound Data Structures:**

```bash
python Exercises/exercicio1.py
```

Expected output:

```
==================================================
COMPOUND DATA STRUCTURES
==================================================

1. LIST OF LISTS (3x3 Matrix):
--------------------------------------------------
Matrix: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
First element [0][0]: 1
Element [1][2]: 6
Last row: [7, 8, 9]
```

---

## Topics Covered

### Sessions 1 & 2 — Environment & Version Control
- Information Systems overview
- Version Control Systems (VCS) and Git concepts
- Semantic versioning (MAJOR.MINOR.PATCH)
- Git: commits, branches, remotes, merge, push/pull, tags
- IDEs vs editors — VS Code, PyCharm, IntelliJ

### Sessions 3 & 4 — Markdown & Python Fundamentals
- Basic Git commands (`status`, `clone`, `pull`, `branch`, `checkout`, `commit`, `merge`, `push`)
- Markdown syntax — headings, lists, tables, task lists, code blocks, links
- Python overview — interpreted, dynamically typed, multi-paradigm
- Comments and docstrings (`#`, `'''`, `"""`)
- Variables and naming styles — camelCase, PascalCase, snake_case
- Python data types — `int`, `float`, `complex`, `str`, `bool`, `list`, `tuple`, `dict`, `set`, `frozenset`, `bytes`
- Numeric operations and f-strings
- Boolean algebra and logical operators (`and`, `or`, `not`)
- Compound data structures — list of lists, dict of lists, list of dicts

---

## References

- Costa, E. (2015). *Programação em Python*. FCA.
- Borges, L. (2015). *Python para Desenvolvedores*. Novatec.
- [Markdown Guide](https://www.markdownguide.org)
- [Python Docs](https://docs.python.org/3/)
- [ISTEC — Programming IV Syllabus](https://www.istec.pt/index.php/programacao-iv/)

