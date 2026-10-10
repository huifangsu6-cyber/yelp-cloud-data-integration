"""Synthetic check-in data validation example, not original coursework code."""
from __future__ import annotations

from collections import Counter
from datetime import datetime
from typing import Iterable

DATE_FORMAT = "%Y-%m-%d %H:%M:%S"


def normalise_checkins(records: Iterable[dict[str, str]]) -> tuple[list[dict], dict]:
    """Expand comma-delimited timestamps; preserve and flag repeated events."""
    output: list[dict] = []
    stats: Counter[str] = Counter()
    seen: set[tuple[str, str]] = set()

    for record in records:
        stats["source_rows"] += 1
        business_id = (record.get("business_id") or "").strip()
        if not business_id:
            stats["missing_business_ids"] += 1
            continue
        for token in (record.get("date") or "").split(","):
            raw = token.strip()
            if not raw:
                continue
            stats["timestamp_tokens"] += 1
            try:
                timestamp = datetime.strptime(raw, DATE_FORMAT)
            except ValueError:
                stats["invalid_timestamps"] += 1
                continue
            key = (business_id, timestamp.isoformat())
            if key in seen:
                stats["repeated_event_keys"] += 1
            seen.add(key)
            output.append({
                "business_id": business_id,
                "timestamp": timestamp.isoformat(sep=" "),
                "hour": timestamp.hour,
            })
            stats["valid_events"] += 1
    return output, dict(stats)


if __name__ == "__main__":
    demo = [
        {"business_id": "sample_a", "date": "2024-01-05 18:30:00, 2024-01-06 12:00:00"},
        {"business_id": "sample_b", "date": "bad-date, 2024-01-07 09:00:00"},
    ]
    events, profile = normalise_checkins(demo)
    print("Synthetic events:", events)
    print("Quality profile:", profile)
