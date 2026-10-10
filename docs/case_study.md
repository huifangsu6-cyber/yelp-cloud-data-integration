# Case study: cloud data integration for restaurant analytics

## Context
A university team analysed Yelp business, review and check-in datasets. Before teammates could undertake dataset-specific analysis, the raw files needed a consistent shared data foundation.

## My contribution
I organised and standardised source files in Google Cloud Storage, including file naming, folder structure, CSV/JSON formats, duplicate or irrelevant files, schema inspection and identification of final versions. I designed the GCS-to-BigQuery integration workflow, set up data loading and table structures, and distributed the prepared datasets to teammates.

## Architecture
```text
Yelp source datasets
   |
   v
File inventory and standardisation  <-- My work
   |
   v
Google Cloud Storage organisation   <-- My work
   |
   v
BigQuery loading and schema setup   <-- My work
   |
   v
Shared analytical datasets
   |
   +--> Review analysis             <-- Teammate workstream
   +--> Check-in analysis           <-- Teammate workstream
   +--> Other group analysis
```

## Practical decisions
- **Naming and structure:** classified datasets by type and purpose so collaborators could identify the right inputs.
- **Version control:** selected authoritative dataset versions rather than sharing multiple ambiguous copies.
- **Format and schema:** checked CSV/JSON format and field structures before downstream ingestion.
- **Collaboration:** made prepared datasets available to the appropriate workstreams.

## Evidence and limitations
These responsibilities are based on my account of my work on the group project. The original coursework, teaching materials, collaborator notebooks, cloud credentials and Yelp source data are deliberately **not republished** here. This repository's code is a **new synthetic portfolio demonstration**, not a reproduction of the original cloud deployment.

No production availability, quantified quality improvement or commercial impact is claimed.

## Interview summary
> I prepared the cloud data foundation for a group Yelp analytics project: organising and standardising source files in GCS, checking formats and schemas, setting up BigQuery loading and table structures, and handing off consistent datasets to teammates for their SQL and Python analysis.
