"""Fast boundary checks: monetary false positives and target/config validation."""
from pathlib import Path
import os
import sys
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "libraries"))
sys.path.insert(0, str(ROOT / "variables"))
from QualityLibrary import QualityLibrary
from settings import get_variables

class MonetaryOracleTests(unittest.TestCase):
    def setUp(self):
        self.oracle = QualityLibrary()

    def test_valid_totals_are_calculated_from_all_lines(self):
        self.oracle.totals_should_be_consistent(["$29.99", "$9.99"], "Item total: $39.98", "Tax: $3.20", "Total: $43.18")

    def test_cent_rounding(self):
        self.oracle.totals_should_be_consistent(["$0.07"], "Item total: $0.07", "Tax: $0.01", "Total: $0.08")

    def test_inconsistent_components_are_rejected_independently(self):
        for subtotal, tax, total in [("$40.00", "$3.20", "$43.18"), ("$39.98", "$3.19", "$43.18"), ("$39.98", "$3.20", "$43.19")]:
            with self.subTest(subtotal=subtotal, tax=tax, total=total), self.assertRaises(AssertionError):
                self.oracle.totals_should_be_consistent(["$29.99", "$9.99"], subtotal, tax, total)

    def test_malformed_currency_does_not_silently_pass(self):
        for value in ["USD 29.99", "$29,99", "$29.999", "-$29.99", "Total: $29.99 extra"]:
            with self.subTest(value=value), self.assertRaises(AssertionError):
                self.oracle.prices_should_be_ascending(["$1.00", value])

    def test_duplicates_in_sorted_prices_are_valid(self):
        self.oracle.prices_should_be_ascending(["$7.99", "$15.99", "$15.99"])

    def test_unsorted_or_too_small_catalog_is_rejected(self):
        for values in [[], ["$1.00"], ["$9.99", "$7.99"]]:
            with self.subTest(values=values), self.assertRaises(AssertionError):
                self.oracle.prices_should_be_ascending(values)

class ConfigurationTests(unittest.TestCase):
    def test_public_and_local_targets_are_allowed(self):
        for target in ["https://www.saucedemo.com/", "https://saucelabs.github.io/sample-app-web/", "http://localhost:3000/"]:
            with self.subTest(target=target), patch.dict(os.environ, {"SD_BASE_URL": target, "SD_TIMEOUT": "10"}, clear=True):
                self.assertEqual(get_variables()["BASE_URL"], target)

    def test_unapproved_targets_and_credentials_are_rejected(self):
        for target in ["https://example.com/", "https://private:secret@www.saucedemo.com/", "http://www.saucedemo.com/", "https://www.saucedemo.com/?token=abc"]:
            with self.subTest(target=target), patch.dict(os.environ, {"SD_BASE_URL": target}, clear=True), self.assertRaises(ValueError):
                get_variables()

    def test_timeout_bounds_are_enforced(self):
        for timeout in ["0", "61", "invalid"]:
            with self.subTest(timeout=timeout), patch.dict(os.environ, {"SD_TIMEOUT": timeout}, clear=True), self.assertRaises(ValueError):
                get_variables()

if __name__ == "__main__":
    unittest.main()
