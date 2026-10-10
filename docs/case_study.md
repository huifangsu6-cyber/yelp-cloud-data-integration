# Case Study: Preparing Yelp Data for Cloud Analytics

## Project background

Our university team explored restaurant performance using Yelp business, review and check-in datasets. The first challenge was bringing files with different structures and formats into a shared environment so the analysis workstreams could use consistent inputs.

## My role: cloud data integration

I was responsible for preparing the shared data foundation using **Google Cloud Storage (GCS)** and **BigQuery**.

| Area | What I did |
| --- | --- |
| File organisation | Structured cloud storage by dataset type and purpose |
| Data standardisation | Standardised file names and CSV/JSON formats |
| Dataset management | Removed duplicate or irrelevant files and identified final versions |
| Schema readiness | Reviewed fields and file structures before loading |
| Cloud integration | Designed the GCS-to-BigQuery workflow and set up loading and table structures |
| Team hand-off | Distributed prepared datasets to teammates for analysis |

## Data flow

```text
Yelp source files
       |
       v
Inventory, standardisation and schema review
       |
       v
Google Cloud Storage
       |
       v
BigQuery loading and tables
       |
       v
Shared datasets for team analysis
```

## Technical decisions

### Consistent storage structure
Organising files by data type and purpose made it easier for the team to locate the correct inputs and work from a common dataset structure.

### Reliable file versions
I reviewed redundant files and established which versions should be used for downstream work, reducing ambiguity during collaboration.

### Preparing data for BigQuery
I checked the formats and fields of source datasets and set up the loading workflow and table structures needed for SQL analysis.

### Supporting parallel analysis
Once the datasets were organised and loaded, teammates could work on their respective review, check-in and other analytical tasks using the shared data foundation.

## Related examples

- [Source manifest validation](../src/source_manifest.py) — file metadata, path, format and version checks.
- [BigQuery SQL quality checks](../sql/checkin_quality_checks.sql) — example SQL for profiling timestamps.
- [Python data validation](../src/checkin_quality.py) — example timestamp parsing and error counts.

These examples use sample data and illustrate techniques relevant to the project.

## Skills

Google Cloud Storage · BigQuery · Data Integration · Data Standardisation · Schema Review · Data Quality · Team Collaboration
