# Week 1 — Local Prototype (Phase 1)

**Goal:** Get data flowing from YouTube through Bronze → Silver → Gold locally.
**Time:** 1 hour/day × 5 days

---

## Day 1 — Project Setup + Explore YouTube API

- Create the local folder structure: `data/bronze/youtube/`, `data/silver/`, `data/gold/`
- Run `youtube_test.py` and inspect the raw API response carefully
- Ask yourself: what fields does YouTube give you? Which ones are useful for trend scoring?
- Decide what fields to keep in Bronze

**Goal by end of day:** Know exactly what your raw data looks like.

---

## Day 2 — Ingestion Script (Bronze Layer)

- Build `ingestion/youtube.py` — a script that searches YouTube for mechanical keyboard videos and saves the raw response as JSON to `data/bronze/youtube/`
- Each run should save a new file (think about how to name it — hint: timestamps)
- Do not clean or transform anything here

**Goal by end of day:** Running the script produces a raw JSON file in Bronze.

---

## Day 3 — Processing (Silver Layer)

- Build `processing/silver.py` — reads Bronze JSON, cleans and normalizes it
- Tasks: remove duplicates, standardize fields, extract product mentions (dictionary approach for now)
- Save output as Parquet to `data/silver/`
- Look up: what is Parquet and why use it over JSON for processed data?

**Goal by end of day:** Running the script produces a clean Parquet file in Silver.

---

## Day 4 — Trend Scoring (Gold Layer)

- Build `processing/gold.py` — reads Silver Parquet, applies trend score formula, outputs top 3
- Adapt the formula fields to what YouTube actually gives you
- Save output as Parquet to `data/gold/`

**Goal by end of day:** Running gold.py prints (or saves) the top 3 trending keyboards.

---

## Day 5 — End-to-End Run + Review

- Run the full pipeline manually: ingest → silver → gold
- Check the output — does it make sense? Are the results reasonable?
- Note anything broken or surprising
- Update `spec.md` if anything changed during building

**Goal by end of day:** One clean end-to-end run with real YouTube data.

---

## Out of Scope This Week

- Scheduling / cron
- Reddit ingestion
- Dashboard
- Cloud / AWS
