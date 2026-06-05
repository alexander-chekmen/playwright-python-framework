"""Project-wide pytest configuration.

Holds only app-agnostic plumbing. App-specific fixtures live in the nested
``conftest.py`` under each ``tests/<app>/`` directory.
"""

import logging
import pytest

# Here you can change Playwright's default 30000 timeout, helpful when debugging locally
DEFAULT_TIMEOUT_MS = 30000

def pytest_configure(config):
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
    )

@pytest.fixture(autouse=True)
def _set_default_timeout(page):
    """Cap Playwright's default action and navigation timeouts for every test.

    Autouse, so it applies to each test's 'page' without being requested.
    Overrides Playwright's 30s built-in default with 'DEFAULT_TIMEOUT_MS',
    making element waits (clicks, fills, 'wait_for', auto-waiting queries)
    and navigations ('goto', 'wait_for_url') fail faster.

    Does not affect 'expect(...)' assertions, which keep their own default;
    individual calls can still override via a 'timeout' argument.
    """
    page.set_default_timeout(DEFAULT_TIMEOUT_MS)
    page.set_default_navigation_timeout(DEFAULT_TIMEOUT_MS)
