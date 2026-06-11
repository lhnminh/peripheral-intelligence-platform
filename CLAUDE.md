# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

A data aggregation platform that collects peripheral (keyboards, mice, etc.) data from multiple sources (YouTube, Reddit, Google APIs) to surface trends and help guide purchasing decisions.

## Package Manager & Environment

This project uses **uv** for dependency management.

```bash
# Install dependencies
uv sync

# Run a script
uv run python main.py
uv run python youtube_test.py

# Add a dependency
uv add <package>

# Add a dev dependency
uv add --dev <package>
```

Requires Python 3.13+ (see `.python-version`).

## Environment Variables

Copy `.env` and populate it before running anything:
- `YOUTUBE_API_KEY` — YouTube Data API v3 key (used in `youtube_test.py`)

## Architecture

The platform is designed around three layers:

1. **Data ingestion** — API clients for external sources:
   - YouTube: `google-api-python-client` (sync)
   - Reddit: `praw` (sync) / `asyncpraw` (async)

2. **Data processing** — `pandas` + `pyarrow` for transformation and columnar storage; `duckdb` for analytical queries in dev; `sqlalchemy` for persistence.

3. **Entry point** — `main.py` is currently a stub. New data source modules should be importable from here.

`youtube_test.py` is the reference implementation for the API client pattern: load key from `.env` via `dotenv`, instantiate the API client, execute queries, extract structured metadata.

## Collaboration Style

The user is learning Data Engineering through this project. Prefer:
- Pointing to relevant concepts, docs, or patterns to explore rather than writing code directly
- Asking guiding questions that lead to the solution
- Explaining *why* something is done, not just *what* to do
- Suggesting what to read or experiment with next
