# Cloud Data Integration | Yelp Analytics Portfolio

**Google Cloud Storage · BigQuery · Python · SQL · Data Quality · Data Governance**

A focused portfolio case study about the **cloud data foundation I personally prepared** for a collaborative university Yelp restaurant analytics project.

> **My role:** I organised and standardised source datasets in Google Cloud Storage, reviewed file formats and schemas, identified final dataset versions, and designed the shared GCS → BigQuery loading and table setup workflow. Teammates carried out their own dataset-specific cleaning and analytical workstreams.

## Featured case study

**[Read: Cloud Data Integration & Data Governance](docs/case_study.md)**

The case study explains the business problem, my responsibilities, key data-management decisions and the hand-off to the analysis team.

```text
Yelp source files
    |
    v
Inventory, naming, version selection, format/schema checks  [my work]
    |
    v
Google Cloud Storage organisation                         [my work]
    |
    v
BigQuery data loading and table structure                 [my work]
    |
    v
Shared analytical data
    |
    +--> Review, check-in and other analysis              [team workstreams]
```

## Repository guide

| Resource | What it demonstrates |
| --- | --- |
| [Individual case study](docs/case_study.md) | My GCS/BigQuery data integration responsibilities |
| [Architecture](docs/architecture.md) | Data flow, quality gates and responsibility boundaries |
| [Data governance](docs/data_governance.md) | File organisation, schema readiness and dataset hand-off |
| [Python example](src/checkin_quality.py) | Newly written synthetic timestamp validation |
| [SQL example](sql/checkin_quality_checks.sql) | Read-only BigQuery Standard SQL quality profile |
| [Unit tests](tests/test_checkin_quality.py) | Input validation and duplicate detection |
| [Synthetic sample](sample_data/synthetic_checkins.csv) | Fictional data only |

## Run the Python example

Requires **Python 3.10+**. No cloud account, API key or third-party package required.

```bash
python src/checkin_quality.py
python -m unittest discover -s tests -v
```

The Python and SQL examples were **created separately as portfolio illustrations**. In particular, the original project's check-in analysis was a teammate workstream; this example is not presented as my original contribution.

## Project context and limitations

The original academic project combined multiple Yelp datasets to explore restaurant performance. This repository is **not a copy of the coursework** and does not include course tutorials, other group members' code, original reports, Yelp records or cloud credentials.

The cloud integration responsibilities described above are based on my direct account of my work. The original cloud pipeline is not deployed or reproduced here, and no commercial impact or production-readiness claim is made.

**Target roles:** Data Analyst · Junior Data Engineer · BI / Data Quality Analyst
