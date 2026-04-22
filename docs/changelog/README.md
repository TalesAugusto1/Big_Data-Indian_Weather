# Changelog entries

This folder records **major development** work on the repo (features, notable tooling, structural changes). Each entry is its own Markdown file so history stays easy to browse and link from PRs or tasks.

## Convention

- **One file per major change** (or one cohesive feature), named `YYYY-MM-DD-short-slug.md` using the date the work landed (or the main commit date).
- Include: **summary**, **why**, **what changed** (paths, APIs), **how to run** or verify, **dependencies**, and **follow-ups** if any.
- New entries are listed below (newest first).

## Index

| Date | Slug | Summary |
|------|------|---------|
| 2026-04-21 | [docker-compose-m01](2026-04-21-docker-compose-m01.md) | `docker-compose.yml` + `docker/hadoop.env` + health checks (M01 / T011) |
| 2026-04-21 | [stack-apache-m01](2026-04-21-stack-apache-m01.md) | Documentação do stack Docker Apache (HDFS, YARN, Spark) para M01 / T010 (`docs/stack-apache.md`) |
| 2026-04-21 | [csv-to-parquet-streaming](2026-04-21-csv-to-parquet-streaming.md) | Streaming de CSV para Parquet com PyArrow (`scripts/csv_to_parquet.py`) |

## Related

- User-facing runbook: [README.md](../../README.md) (venv, `csv_to_parquet.py` flags).
- Course scope: [core.md](../../core.md).
- Task tracking: [storyline/README.md](../../storyline/README.md).
