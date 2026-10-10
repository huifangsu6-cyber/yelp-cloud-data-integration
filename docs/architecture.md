# Architecture and responsibility boundaries

```text
Source JSON / CSV
      |
      | inventory, file naming, format checks, version selection
      v
Google Cloud Storage (GCS)
      |
      | organised bucket and dataset structure
      v
BigQuery ingestion
      |
      | schema review, table setup and loading
      v
Shared datasets
      |
      +-- downstream SQL and Python analysis (collaborative)
```

**Original implementation:** GCS and BigQuery were used in the university group project. Specific bucket names, access policies and production orchestration are intentionally not reproduced here.

**This repository:** a self-contained Python demonstration with invented records. It illustrates validation and transformation techniques but does not connect to GCS or BigQuery.

### Quality gates worth applying to a real pipeline
1. Verify source file type and expected schema.
2. Check source row counts and null business identifiers.
3. Parse timestamps with explicit error handling.
4. Record duplicate identifiers/timestamps without silently discarding events.
5. Reconcile valid, invalid and missing-record counts.
6. Document data ownership and hand-off.

These are recommended controls, not a claim that all were automated in the original coursework.
