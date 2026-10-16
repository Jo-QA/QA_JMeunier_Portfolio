"""Small Python boundary: browser lifecycle, Decimal oracles, evidence metadata.

The page resources own the selectors. Tests own the business expectations.
"""
import json
import os
import platform
import re
from datetime import datetime, timezone
from decimal import Decimal, ROUND_HALF_UP
from importlib.metadata import version
from pathlib import Path
from robot.api.deco import keyword, library
from robot.libraries.BuiltIn import BuiltIn
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from SeleniumLibrary.errors import NoOpenBrowser

@library(scope="SUITE", auto_keywords=False)
class QualityLibrary:
    @staticmethod
    def _sl():
        return BuiltIn().get_library_instance("SeleniumLibrary")

    @keyword
    def open_isolated_chrome(self):
        """Selenium creates a fresh temporary profile for every test."""
        options = webdriver.ChromeOptions()
        if os.getenv("SD_HEADLESS", "true").lower() in {"1", "true", "yes"}:
            options.add_argument("--headless=new")
        options.add_argument("--window-size=1440,1000")
        options.add_argument("--disable-dev-shm-usage")
        options.add_experimental_option("prefs", {
            "credentials_enable_service": False,
            "profile.password_manager_enabled": False,
            "profile.password_manager_leak_detection": False,
        })
        if os.getenv("SD_BROWSER_BINARY"):
            options.binary_location = os.environ["SD_BROWSER_BINARY"]
        os.environ.setdefault("SE_AVOID_STATS", "true")
        service = Service(executable_path=os.environ["SD_DRIVER_PATH"]) if os.getenv("SD_DRIVER_PATH") else Service()
        index = self._sl().create_webdriver("Chrome", options=options, service=service)
        driver = self._sl().driver
        driver.set_page_load_timeout(30)
        driver.set_window_size(1440, 1000)
        caps = driver.capabilities
        metadata = {
            "captured_at_utc": datetime.now(timezone.utc).isoformat(),
            "python": platform.python_version(), "os": platform.system(),
            "system_timezone": str(datetime.now().astimezone().tzinfo),
            "browser": caps.get("browserName"), "browser_version": caps.get("browserVersion"),
            "driver_version": caps.get("chrome", {}).get("chromedriverVersion", "").split(" ")[0],
            "packages": {name: version(name) for name in ["robotframework", "robotframework-seleniumlibrary", "selenium"]},
            "base_url": BuiltIn().get_variable_value("${BASE_URL}"),
            "headless": os.getenv("SD_HEADLESS", "true"),
            "viewport": driver.get_window_size(),
        }
        output = Path(BuiltIn().get_variable_value("${OUTPUT DIR}"))
        (output / "environment.json").write_text(json.dumps(metadata, indent=2), encoding="utf-8")
        return index

    @staticmethod
    def _money(text):
        # Strict USD parsing: no floating-point error or silent extraction of arbitrary digits.
        match = re.fullmatch(r"(?:Item total: |Tax: |Total: )?\$(\d+\.\d{2})", text.strip())
        if not match:
            raise AssertionError(f"Invalid USD amount: {text!r}")
        return Decimal(match.group(1))

    @keyword
    def prices_should_be_ascending(self, texts):
        amounts = [self._money(t) for t in texts]
        if len(amounts) < 2 or amounts != sorted(amounts):
            raise AssertionError(f"Prices are not ascending: {amounts}")

    @keyword
    def totals_should_be_consistent(self, line_prices, subtotal_text, tax_text, total_text):
        """Tax rate 8% is an explicit inferred oracle H-11, not a customer requirement."""
        expected = sum((self._money(t) for t in line_prices), Decimal("0.00"))
        subtotal, tax, total = [self._money(t) for t in (subtotal_text, tax_text, total_text)]
        expected_tax = (expected * Decimal("0.08")).quantize(Decimal("0.01"), rounding=ROUND_HALF_UP)
        if (subtotal, tax, total) != (expected, expected_tax, expected + expected_tax):
            raise AssertionError(f"Amounts differ: actual={(subtotal,tax,total)}, expected={(expected,expected_tax,expected+expected_tax)}")

    @keyword
    def capture_test_evidence(self):
        """Screenshots after assertions, also on failure; no screenshot when setup has no browser."""
        sl = self._sl()
        try:
            sl.driver
        except NoOpenBrowser:
            return
        name = BuiltIn().get_variable_value("${TEST NAME}", "test")
        case_id = name.split()[0]
        filename = re.sub(r"[^A-Za-z0-9_-]", "_", case_id) + ".png"
        sl.capture_page_screenshot(filename)
