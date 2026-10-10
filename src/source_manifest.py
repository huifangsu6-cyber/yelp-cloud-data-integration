"""Validate an invented dataset manifest before cloud ingestion.

New portfolio illustration only: does not access GCS or BigQuery.
"""
from __future__ import annotations

from collections import Counter
from pathlib import PurePosixPath
from typing import Any

REQUIRED_FIELDS = ("dataset", "object_path", "format", "version", "columns")
ALLOWED_FORMATS = {"csv", "json"}


def validate_manifest(rows: list[dict[str, Any]]) -> dict[str, Any]:
    """Return a deterministic data-quality summary without changing input."""
    problems: list[str] = []
    seen_paths: set[str] = set()
    seen_versions: set[tuple[str, str]] = set()
    formats: Counter[str] = Counter()

    for index, row in enumerate(rows, start=1):
        missing = [field for field in REQUIRED_FIELDS if not row.get(field)]
        if missing:
            problems.append(f"row {index}: missing {', '.join(missing)}")
            continue

        dataset = str(row["dataset"]).strip()
        object_path = str(row["object_path"]).strip()
        file_format = str(row["format"]).strip().lower()
        version = str(row["version"]).strip()
        columns = row["columns"]
        formats[file_format] += 1

        if file_format not in ALLOWED_FORMATS:
            problems.append(f"row {index}: unsupported format {file_format}")
        if not isinstance(columns, list) or not columns or not all(
            isinstance(column, str) and column.strip() for column in columns
        ):
            problems.append(f"row {index}: invalid columns list")
        if object_path.startswith("/") or ".." in PurePosixPath(object_path).parts:
            problems.append(f"row {index}: unsafe object path")
        if PurePosixPath(object_path).suffix.lower() != f".{file_format}":
            problems.append(f"row {index}: extension does not match format")
        if object_path in seen_paths:
            problems.append(f"row {index}: duplicate object path")
        seen_paths.add(object_path)
        key = (dataset, version)
        if key in seen_versions:
            problems.append(f"row {index}: repeated dataset/version")
        seen_versions.add(key)

    return {
        "source_files": len(rows),
        "format_counts": dict(formats),
        "issue_count": len(problems),
        "issues": problems,
    }


if __name__ == "__main__":
    import json
    from pathlib import Path

    path = Path(__file__).resolve().parents[1] / "sample_data" / "synthetic_manifest.json"
    print(json.dumps(validate_manifest(json.loads(path.read_text())), indent=2))
