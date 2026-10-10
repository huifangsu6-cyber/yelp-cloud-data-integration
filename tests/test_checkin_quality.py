"""Unit tests for the synthetic portfolio example."""
import sys
import unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "src"))
from checkin_quality import normalise_checkins


class CheckinQualityTests(unittest.TestCase):
    def test_split(self):
        rows, stats = normalise_checkins([{"business_id": " A ", "date": "2024-01-05 18:30:00,2024-01-06 12:00:00"}])
        self.assertEqual(len(rows), 2)
        self.assertEqual(rows[0]["business_id"], "A")
        self.assertEqual(rows[0]["hour"], 18)
        self.assertEqual(stats["valid_events"], 2)

    def test_invalid_and_missing(self):
        rows, stats = normalise_checkins([
            {"business_id": "A", "date": "invalid,2024-01-05 18:30:00"},
            {"business_id": "", "date": "2024-01-05 18:30:00"},
        ])
        self.assertEqual(len(rows), 1)
        self.assertEqual(stats["invalid_timestamps"], 1)
        self.assertEqual(stats["missing_business_ids"], 1)

    def test_duplicates_are_flagged(self):
        rows, stats = normalise_checkins([{"business_id": "A", "date": "2024-01-05 18:30:00,2024-01-05 18:30:00"}])
        self.assertEqual(len(rows), 2)
        self.assertEqual(stats["repeated_event_keys"], 1)

    def test_empty(self):
        self.assertEqual(normalise_checkins([]), ([], {}))


if __name__ == "__main__":
    unittest.main()
