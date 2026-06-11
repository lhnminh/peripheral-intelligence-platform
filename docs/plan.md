# Project Plan

## Steps

1. Start with mechanical keyboards.
2. Ingest YouTube data.
3. Save raw JSON to `data/bronze/`.
4. Clean data into `data/silver/`.
5. Extract product mentions.
6. Run sentiment analysis.
7. Create rankings in `data/gold/`.
8. Build a small dashboard.
9. Containerize with Docker.
10. Deploy the dashboard with Vercel.

## MVP

- Top 3 trending mechanical keyboards.
- YouTube first.
- Reddit later.
- Local first, cloud later.

## Metrics

- Mention count
- Engagement score
- Sentiment
- Trend score

## Technologies

- Python
- YouTube Data API
- Reddit API later
- Pandas
- DuckDB
- SQL
- Parquet
- Sentiment analysis model
- Streamlit or Vercel frontend
- Vercel
- Docker
- GitHub Actions
- AWS S3 later
- Databricks later
- Spark later
