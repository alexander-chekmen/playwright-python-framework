# conftest.py - shared pytest fixtures for Playwright browser setup

import pytest
import logging
from playwright.sync_api import sync_playwright


@pytest.fixture(scope="function")
def page(request):
    # By default playwright will run in headless mode.
    # To run it in headed mode use --headed in pytest.
    headed = request.config.getoption("--headed")

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=not headed)

        context = browser.new_context()
        page = context.new_page()

        yield page

        context.close()
        browser.close()

def setup_logging():
    logging.basicConfig(
        level=logging.INFO,
        format="\n%(asctime)s - %(levelname)s - %(message)s"
    )

setup_logging()


# This adds a separator between each test in a console for readability
def pytest_runtest_logreport(report):
    if report.when == "call":
        print("\n" + "-" * 60)