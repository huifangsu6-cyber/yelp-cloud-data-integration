"""Tests for the synthetic pre-ingestion manifest validation example."""
import json
import sys
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "src"))
from source_manifest import validate_manifest


class ManifestTests(unittest.TestCase):
    def test_valid_example(self):
        data = json.loads((ROOT / "sample_data" / "synthetic_manifest.json").read_text())
        result = validate_manifest(data)
        self.assertEqual(result["source_files"], 3)
        self.assertEqual(result["issue_count"], 0)

    def test_missing_field(self):
        result = validate_manifest([{"dataset": "business"}])
        self.assertEqual(result["issue_count"], 1)

    def test_duplicate_path_and_version(self):
        row = {"dataset": "business", "object_path": "raw/business.json",
               "format": "json", "version": "v1", "columns": ["id"]}
        result = validate_manifest([row, row.copy()])
        self.assertEqual(result["issue_count"], 2)

    def test_unsafe_path_and_format_mismatch(self):
        result = validate_manifest([{"dataset": "business",
            "object_path": "../business.csv", "format": "json",
            "version": "v1", "columns": ["id"]}])
        self.assertEqual(result["issue_count"], 2)


if __name__ == "__main__":
    unittest.main()
