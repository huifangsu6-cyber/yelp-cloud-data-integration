# Data Quality Validation — Example Output

The examples run locally using synthetic data, without cloud credentials or external dependencies.

## Dataset manifest checks

Run:

```bash
python src/source_manifest.py
```

Expected output for [the sample manifest](../sample_data/synthetic_manifest.json):

```json
{
  "source_files": 3,
  "format_counts": {
    "json": 2,
    "csv": 1
  },
  "issue_count": 0,
  "issues": []
}
```

The manifest includes three sample datasets (business, review and check-in). The validator checks file paths, extensions, declared formats, version combinations and column metadata.

## Check-in quality profiling

Run:

```bash
python src/checkin_quality.py
```

For the built-in two-row sample, the validator produces **3 valid events** and **1 invalid timestamp**, illustrating how parsing issues can be counted before analysis.

## Automated tests

```bash
python -m unittest discover -s tests -v
```

The test suite contains **8 tests** covering timestamp parsing, missing identifiers, duplicate event keys, manifest fields, duplicate file/version entries and invalid paths.

See [GitHub Actions](../.github/workflows/python-tests.yml) for the automated verification workflow. The example output above is from the synthetic inputs, not the original Yelp dataset.
