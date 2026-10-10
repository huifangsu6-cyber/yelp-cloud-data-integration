# Data Organisation & Quality

Preparing a reliable dataset starts before SQL analysis. The project involved organising multiple Yelp source files so teammates could use a consistent shared data foundation.

## Data preparation practices

| Focus | Approach | Why it matters |
| --- | --- | --- |
| Dataset organisation | Group files by dataset type and purpose | Easier discovery and hand-off |
| File naming | Apply consistent naming conventions | Less confusion across workstreams |
| Version management | Identify final datasets and remove redundant copies | More consistent analysis inputs |
| Format standardisation | Review CSV/JSON formats | Predictable ingestion |
| Schema review | Inspect fields and data structures | Better BigQuery loading readiness |
| Collaboration | Share prepared datasets by workstream | Supports parallel analysis |

## Example quality checks

The [source manifest validator](../src/source_manifest.py) demonstrates how file metadata can be checked before ingestion. It reports missing fields, repeated paths and versions, unsupported formats, and invalid column definitions.

The [check-in quality example](../src/checkin_quality.py) illustrates timestamp parsing, error counts and duplicate event detection using synthetic records.
