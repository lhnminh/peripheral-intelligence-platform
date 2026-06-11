# AGENTS.md

## Collaboration Style

- Explain changes step by step before and while making them.
- Keep edits small and scoped to the current request.
- Do not make unrelated refactors or cleanup changes.
- Before editing files, state which files will be changed and why.
- After editing files, summarize what changed and how to verify it.

## Learning Mode

- The user wants to do a lot of the coding themselves because the main goal is to learn.
- Prefer teaching, planning, reviewing, and giving small guided next steps before writing code.
- When code changes are useful, ask whether to implement them or provide instructions for the user to implement.
- Explain the reasoning behind design choices, tradeoffs, and debugging steps.
- Avoid large automatic implementations unless the user explicitly asks Codex to make the changes.

## Project Direction

This repository is for building an end-to-end sentiment analysis and data engineering pipeline for computer peripheral purchasing research.

The project should emphasize practical data engineering skills:

- API ingestion
- raw data storage
- data modeling
- SQL transformations
- analytics-ready tables
- sentiment analysis
- AI-assisted text enrichment
- data quality checks
- reproducible local development
- portfolio-quality documentation

## Current Preference

The user wants to understand all changes being made, so step-by-step explanations are preferred over large unexplained edits.

Markdown files should be extremely minimal. Prefer short sections, short bullets, and only the information needed to understand the project.
