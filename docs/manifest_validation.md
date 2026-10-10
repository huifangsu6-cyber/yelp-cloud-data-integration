# Source Manifest Validation

A lightweight Python example for checking dataset metadata before cloud ingestion.

## Why validate a manifest?

When multiple datasets are prepared for a shared analytics environment, a manifest can help track the expected file locations, formats, versions and columns. Checking this metadata early makes hand-offs more consistent.

## Run the example

```bash
python src/source_manifest.py
python -m unittest discover -s tests -v
```

The example reads [sample dataset metadata](../sample_data/synthetic_manifest.json) and reports any validation issues.

## Validation checks

- Required fields: dataset, object path, format, version and columns.
- Supported CSV and JSON formats.
- File extension matches the declared format.
- Duplicate object paths.
- Repeated dataset/version combinations.
- Safe relative file paths.
- Non-empty column definitions.

## Example output

A valid manifest produces a summary with source file counts, format counts and zero issues. Invalid entries generate descriptive issue messages.

This example uses synthetic metadata and runs locally without cloud credentials.
