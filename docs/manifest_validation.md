# Source manifest validation — synthetic portfolio example

This **newly authored** Python example focuses on the cloud-data preparation work described in my case study. It does **not** reproduce the original GCS environment.

## Run locally

```bash
python src/source_manifest.py
python -m unittest discover -s tests -v
```

No third-party dependencies or credentials are required.

The invented manifest in [synthetic_manifest.json](../sample_data/synthetic_manifest.json) describes fictional business, review and check-in files. The validator checks:

- Required metadata: dataset, object path, format, version and columns.
- Supported CSV/JSON formats and filename extensions.
- Duplicate object paths and repeated dataset/version combinations.
- Relative object paths without parent-directory traversal.
- Non-empty lists of column names.

It produces an issue report and format counts; it does not delete files, inspect actual cloud objects, infer schemas, enforce GCS IAM, or load data into BigQuery.

**Why it matters:** Consistent naming, format checks, dataset versions and schema readiness help prevent the team from analysing inconsistent source files.
