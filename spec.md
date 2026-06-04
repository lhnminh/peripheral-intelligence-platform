# Peripheral Intelligence Platform — Spec

## Overview

Cloud-based data engineering project for tracking and ranking trending computer peripherals across online enthusiast communities.

Ingests data from multiple sources (YouTube, Reddit, and others), processes it using Databricks and Spark, and generates trend intelligence for products like mechanical keyboards and gaming mice.

**MVP:** Identify the top 3 trending mechanical keyboards using YouTube data.

---

## Project Goals

Demonstrate modern data engineering concepts:

- Cloud data architecture
- Medallion data modeling
- Distributed processing with Spark
- Delta Lake table management
- Ingestion pipelines
- Trend aggregation
- API serving
- Analytics dashboards
- AI-assisted data enrichment

---

## MVP Scope

**Initial category:** Mechanical keyboards only

**Future categories:** Gaming mice, IEMs, Monitors, Headphones

**Example output:**
```
Top Mechanical Keyboards This Week
1. Wooting 80HE
2. Keychron Q1 HE
3. DrunkDeer A75
```

---

## High-Level Architecture

```
YouTube API (+ Reddit API later)
  ↓
Python Ingestion Service
  ↓
Local Bronze Layer (JSON files)
  ↓
Local Processing (pandas / DuckDB)
  ↓
Local Silver & Gold (Parquet files)
  ↓
Dashboard / Analytics UI
```

Cloud version (Phase 2+):
```
Data Sources
  ↓
Python Ingestion Service
  ↓
AWS S3 Bronze Layer
  ↓
Databricks + Spark Processing
  ↓
Silver Delta Tables
  ↓
Gold Trend Aggregations
  ↓
FastAPI Service
  ↓
Dashboard / Analytics UI
```

---

## Tech Stack

| Layer               | Technology                        |
|---------------------|-----------------------------------|
| Cloud Platform      | AWS                               |
| Object Storage      | S3                                |
| Processing Engine   | Databricks                        |
| Distributed Compute | Apache Spark                      |
| Storage Format      | Delta Lake (cloud) / Parquet (local) |
| Language            | Python                            |
| Transformation      | Spark SQL (cloud) / DuckDB (local) |
| API                 | FastAPI                           |
| Dashboard           | Streamlit                         |
| Containerization    | Docker                            |
| Infrastructure      | Terraform                         |

---

## Data Sources

### Phase 1 — YouTube
- Video titles, channel, published date, view/engagement metrics
- Search queries targeting mechanical keyboard products
- Reference: `youtube_test.py`

### Phase 2+ — Reddit
- Target subreddits: r/MechanicalKeyboards, r/keyboards
- Fields: post title, post body, comments, timestamps, upvotes, engagement metrics

### Future Sources
- Review sites, forums, other enthusiast communities

---

## Data Architecture (Medallion)

### Bronze Layer
- **Purpose:** Store raw ingestion data exactly as received — never modified
- **Local:** `data/bronze/youtube/`, `data/bronze/reddit/`
- **Cloud:** `s3://peripheral-intelligence/bronze/`
- **Format:** Raw JSON files

### Silver Layer
- **Purpose:** Clean, normalize, and AI-enrich data into a consistent schema
- **Processing:**
  1. Remove duplicates, standardize timestamps, clean text, normalize schema
  2. **AI — Product extraction:** LLM identifies product mentions from raw text (replaces hardcoded dictionary long-term)
  3. **AI — Sentiment analysis:** LLM classifies each mention as positive, negative, or neutral
- **Local:** `data/silver/` (Parquet)
- **Cloud:** Delta tables in Databricks (`youtube_videos`, `reddit_posts`, `product_mentions`)

### Gold Layer
- **Purpose:** Analytics-ready trend datasets
- **Metrics:** mention counts, engagement scores, trend momentum, weekly rankings
- **Tables:** `daily_product_rankings`, `weekly_trending_products`

---

## Product Mention Extraction

**MVP approach:** Dictionary-based matching

```python
PRODUCTS = [
    "wooting 80he",
    "keychron q1 he",
    "drunkdeer a75"
]
```

Pipeline: lowercase text → clean formatting → detect product matches → store mentions

**AI upgrade:** LLM-assisted extraction — no hardcoded list needed, handles new products automatically

---

## Trend Scoring

```
TrendScore = 0.5 * MentionCount + 0.3 * Upvotes + 0.2 * CommentCount
```

Fields will be adapted per source (e.g. YouTube views/likes instead of upvotes).

**Future improvements:** recency weighting, momentum detection, rolling averages, source weighting

**AI upgrade:** incorporate sentiment score into formula so negative buzz doesn't inflate rankings

---

## Databricks Processing (Phase 2+)

Spark jobs handle:
- JSON ingestion from S3
- Transformation pipelines
- Aggregation logic
- Delta table writes

---

## API Layer

```
GET /top-products
GET /products/{product_name}
```

---

## Dashboard (Streamlit MVP)

- Top trending keyboards
- Trend scores
- Mention counts
- Ranking history

---

## Project Structure

```
project/
├── ingestion/
├── processing/
├── databricks/
├── spark_jobs/
├── sql/
├── api/
├── dashboard/
├── data/
│   ├── bronze/
│   ├── silver/
│   └── gold/
├── infrastructure/
├── docker/
├── docs/
└── tests/
```

---

## MVP Milestones

### Phase 1 — Local Prototype (YouTube)
Validate ingestion and ranking logic locally using YouTube API.
- YouTube ingestion script
- Product mention extraction
- Trend scoring
- Top 3 ranking generation
- Local Bronze/Silver/Gold folder structure

### Phase 2 — Add Reddit + Cloud Migration
Add Reddit as a second source; move storage and processing to cloud.
- Terraform to provision AWS infrastructure (S3 buckets, IAM roles, Databricks workspace)
- Reddit ingestion script
- S3 integration (Bronze layer)
- Databricks setup
- Delta table creation
- Multi-source trend aggregation

### Phase 3 — Distributed Processing
Productionize data pipelines.
- Spark transformations
- Scheduled jobs
- Partitioned Delta tables

---

## Future Roadmap

**Phase 4:** AI-generated product summaries explaining *why* a product is trending, embedding generation, additional sources

**Phase 5:** Kafka streaming pipelines, Airflow orchestration, data quality monitoring

**Phase 6:** Recommendation engine, AI-generated product summaries, launch monitoring, benchmark aggregation

---

## Long-Term Vision

A scalable hardware intelligence platform capable of tracking product trends, aggregating community discussions, monitoring launches, analyzing reviews, surfacing emerging peripherals, and generating market insights.