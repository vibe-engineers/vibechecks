<p align="center">
  <img width="220px" src="https://raw.githubusercontent.com/vibe-engineers/vibechecks/main/assets/vibechecks.png" />
  <h1 align="center">VibeChecks Developer Guide</h1>
</p>

## Table of Contents
* [Introduction](#introduction)
* [Navigating this Developer Guide](#navigating-this-developer-guide)
* [Setup](#setup)
* [Project Structure](#project-structure)
* [Key Concepts & Design](#key-concepts--design)
* [Code Documentation](#code-documentation)
* [Testing](#testing)
* [Pull Requests](#pull-requests)
* [Final Notes](#final-notes)

<div style="page-break-after: always;"></div>

## Introduction

For an overview of the library, start with the project [*README*](../README.md) and the public [*wiki*](https://github.com/vibe-engineers/vibechecks/wiki). This developer guide assumes familiarity with modern Python packaging (virtual environments, pip) and basic Large Language Model (LLM) usage. The goal here is to help you move quickly inside a compact codebase without being overwhelmed by ceremony.

## Navigating this Developer Guide

We keep the syntax cues simple so you can skim effectively:

| Syntax     | Description                                      |
| ---------- | ------------------------------------------------ |
| `Markdown`| Commands or code snippets (e.g. `hatch run test`) |
| *Italics*  | Files or folders (e.g. *src/vibechecks*)         |
| **Bold**   | Concepts to pay attention to                     |

<div style="page-break-after: always;"></div>

## Setup

VibeChecks targets Python 3.0+ and ships on PyPI. To work on the project locally:

1. Fork and clone the repository.
   ```bash
   git clone https://github.com/<your-user>/vibechecks.git
   cd vibechecks
   ```
2. Create and activate a virtual environment (any tool works — `venv`, `uv`, `conda`).
3. Install dependencies for development.
   ```bash
   python -m pip install -r requirements.txt -r requirements-dev.txt
   ```
4. If you intend to exercise live LLM calls, copy the `.env.template` to create the `.env` file and fill in provider credentials (e.g. `OPENAI_API_KEY`, `GEMINI_API_KEY`).
5. Run the unit tests once to verify the environment.
   ```bash
   hatch run test
   ```

That is enough to iterate on the library. When you want to try VibeChecks inside another project, use the editable install:
```bash
python -m pip install -e .
```

## Project Structure

VibeChecks keeps a lean layout so the moving parts are easy to reason about:

- *src/vibechecks*: Python package published to PyPI.
  - *vibecheck.py*: Home of the **VibeCheck** facade that developers instantiate or decorate with.
  - *config/config.py*: Declarative knobs built on top of `vibetools.VibeConfig`, including the default system instruction.
  - *utils/logger.py*: Central console logger used across the package for consistent output.
- *tests*: Pytest suite for the exported surface area plus helpers under *tests/utils*.
- *examples*: Minimal usage samples.
- *docs/DeveloperGuide.md*: This document.

External dependencies such as `VibeLlmClient`, `VibeConfig`, and logging primitives live in the sibling [**vibetools**](https://github.com/vibe-engineers/vibetools) package. The code here focuses on tailoring those primitives into the developer-friendly interface that ships as `vibechecks`.

## Key Concepts & Design

Although the library is compact, a couple of patterns are worth knowing before you add features:

### VibeCheck facade

`VibeCheck` wraps an underlying `VibeLlmClient`. The constructor normalises incoming configuration by accepting a `VibeCheckConfig`, a plain dictionary, or nothing at all. Its `__call__` contract is intentionally strict: pass a string and receive a boolean as determined by the backing LLM. Keep the API predictable and side-effect free.

### Configuration defaults

`VibeCheckConfig` subclasses `VibeConfig` to seed a default `system_instruction`. This keeps inference prompts consistent while still allowing advanced users to override options like retry counts or temperature. When adding new configuration toggles, prefer extending `VibeCheckConfig` so downstream users inherit sane defaults.

### Logging

`utils.console_logger` provides the only logging surface that library code should touch. This keeps stdout noise minimal and allows the hosting application to redirect or silence messages in one spot.

### Testing boundaries

Tests assert behaviours at the package boundary. Integration with remote models is faked through stubs in *tests/utils* so the suite runs quickly and deterministically. When contributing new features, extend the stubs rather than talking to live APIs.

## Code Documentation

Keep docstrings and inline comments short but purposeful:

- Every public module, class, and function should have a brief docstring summarising intent.
- Use Google-style docstrings to align with `darglint` checks.
- Add inline comments sparingly for non-obvious logic or TODOs (`# todo: investigate retry jitter`).

Consistent documentation keeps linting green (`hatch run lint`) and lowers the barrier for new contributors.

## Testing

Quality gates are lightweight and fast:

- `hatch run lint` → Runs `darglint`, `ruff`, and `black --check` over *src*.
- `hatch run test` → Executes the pytest suite under *tests*.

Run both before opening a pull request. If you touch packaging metadata, also sanity-check distribution builds with `hatch build`.

## Pull Requests

We favour small, well-scoped changes with clear intent:

1. Branch from `main` in your fork and keep the commit history tidy.
2. Update documentation or examples whenever you change public behaviour.
3. Fill in the pull request template, including screenshots or logs when relevant.
4. Tag reviewers if the change affects external APIs or published packages.

Discuss larger roadmap items in an issue or on [Discord](https://discord.gg/dBW35GBCPZ) before investing significant effort.

## Final Notes

This guide will evolve with the codebase. If you spot gaps or outdated advice, open a quick pull request to fix it — documentation is part of the product. Happy vibing!
