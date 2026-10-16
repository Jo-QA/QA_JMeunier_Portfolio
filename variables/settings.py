"""Robot variable file. Public demo defaults; never print environment secrets."""
import os
from urllib.parse import urlsplit

def get_variables():
    base_url = os.getenv("SD_BASE_URL", "https://www.saucedemo.com/").rstrip("/") + "/"
    parsed = urlsplit(base_url)
    allowed = {"www.saucedemo.com", "saucedemo.com", "saucelabs.github.io", "localhost", "127.0.0.1"}
    if parsed.hostname not in allowed or parsed.username or parsed.password:
        raise ValueError("SD_BASE_URL must point to the public demo or localhost, without credentials")
    if parsed.scheme != "https" and not (parsed.scheme == "http" and parsed.hostname in {"localhost", "127.0.0.1"}):
        raise ValueError("Use HTTPS, or HTTP on localhost")
    if parsed.query or parsed.fragment:
        raise ValueError("SD_BASE_URL must not have query parameters or fragments")
    timeout = int(os.getenv("SD_TIMEOUT", "10"))
    if not 1 <= timeout <= 60:
        raise ValueError("SD_TIMEOUT must be between 1 and 60 seconds")
    return {"BASE_URL": base_url,
            "DEMO_USERNAME": os.getenv("SD_USERNAME", "standard_user"),
            "DEMO_PASSWORD": os.getenv("SD_PASSWORD", "secret_sauce"),
            "LOCKED_USERNAME": os.getenv("SD_LOCKED_USERNAME", "locked_out_user"),
            "UI_TIMEOUT": f"{timeout} seconds"}
