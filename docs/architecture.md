# Data Architecture

## Cloud analytics workflow

```text
Yelp datasets
(JSON / CSV)
      |
      v
Source preparation
- Dataset inventory
- File naming and formats
- Version selection
- Schema review
      |
      v
Google Cloud Storage
- Organised source files
- Shared dataset structure
      |
      v
BigQuery
- Data loading
- Table setup
      |
      v
Analytics-ready shared datasets
      |
      v
Team analysis (SQL / Python)
```

## Key design considerations

| Stage | Focus |
| --- | --- |
| Source preparation | Consistent filenames, formats and final versions |
| Cloud storage | Predictable dataset organisation |
| BigQuery ingestion | Compatible fields and table structures |
| Team hand-off | Clear, consistent datasets for parallel analysis |

## Data quality checkpoints

The included Python and SQL examples illustrate practical checks that complement this workflow:

1. Check required file metadata and expected columns.
2. Identify repeated file paths or dataset versions.
3. Verify file formats and extensions.
4. Parse timestamps and count invalid values.
5. Report duplicate event keys.

See the [source manifest validator](../src/source_manifest.py) and [SQL quality checks](../sql/checkin_quality_checks.sql) for runnable examples.
