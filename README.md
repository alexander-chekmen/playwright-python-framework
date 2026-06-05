# Playwright Python Automation Framework

![tests](https://github.com/alexander-chekmen/playwright-python-framework/actions/workflows/ci.yml/badge.svg)
![python](https://img.shields.io/badge/python-3.12-blue)
![playwright](https://img.shields.io/badge/playwright-1.59-green)
![license](https://img.shields.io/badge/license-MIT-lightgrey)

A UI test-automation framework built with **Playwright** and **pytest**, using the
**Page Object Model**. It is structured to host multiple target applications side by
side — the first suite covers the public [OrangeHRM demo](https://opensource-demo.orangehrmlive.com).

## Features

- **Page Object Model** — locators and actions live in page classes, keeping tests readable.
- **Multi-app layout** — add a new application by dropping a folder under `tests/`, `pages/`, `config/`.
- **Failure artifacts** — screenshot, trace, and video captured automatically on failure.
- **Retries** — optional re-run of flaky tests via `pytest-rerunfailures`.
- **Test markers** — `smoke` and custom markets for targeted runs.
- **HTML reports** — self-contained report via `pytest-html`.
- **CI** — runs on every push/PR through GitHub Actions.

## Tech stack

| Tool | Purpose                                   |
|------|-------------------------------------------|
| Playwright | Browser automation                        |
| pytest + pytest-playwright | Test runner & Playwright fixtures         |
| pytest-html | HTML reports                              |
| pytest-rerunfailures | Retry flaky tests                         |

## Project structure

```
playwright-python-framework/
├── conftest.py                     # project-wide plumbing (logging, default timeouts)
├── pytest.ini                      # pytest config, markers, artifact flags
├── requirements.txt
│
├── config/                         # per-app configuration
│   └── orangehrm.py                # base/login/dashboard URLs
│
├── pages/                          # page objects, grouped by app
│   └── orangehrm/
│       ├── login_page.py
│       └── dashboard_page.py
│
└── tests/                          # tests, grouped by app
    └── orangehrm/
        ├── conftest.py             # OrangeHRM-scope
        ├── test_authentication.py
        └── test_dashboard.py
```

## Getting started

**Prerequisites:** Python 3.12+

```bash
# 1. Clone
git clone https://github.com/alexander-chekmen/playwright-python-framework.git
cd playwright-python-framework

# 2. Create & activate a virtual environment
python -m venv .venv
source .venv/bin/activate          # Windows: .venv\Scripts\activate)

# 3. Install dependencies
pip install -r requirements.txt

# 4. Install Playwright browsers
playwright install
```

## Running the tests

```bash
# Everything
pytest

# A single app
pytest tests/orangehrm

# By marker
pytest -m smoke

# A single test
pytest tests/orangehrm/test_authentication.py::TestAuthentication::test_logout

# Watch it run in a browser
pytest --headed --slowmo 300

# A specific browser (chromium | firefox | webkit)
pytest --browser firefox
```

> Always run through the virtual environment (`source .venv/bin/activate` or
> `.venv/bin/pytest`) so local runs match CI.

## Reports & debugging

Failure artifacts are written to `test-results/`

```bash
# Run tests and generate an HTML report
pytest --html=reports/report.html

# Open a captured trace (timeline, DOM snapshots, network)
playwright show-trace test-results/<test-folder>/trace.zip
```

| Default flags (set in `pytest.ini`) | Behaviour        |
|-------------------------------------|------------------|
| `--screenshot=only-on-failure`      | PNG on failure   |
| `--tracing=retain-on-failure`       | Trace on failure |
| `--video=retain-on-failure`         | Video on failure |



## Continuous integration

GitHub Actions (`.github/workflows/ci.yml`) installs dependencies and browsers,
runs the suite on every push and pull request, and uploads test artifacts (HTML
report, traces, screenshots) for download from the run summary.


## License

[MIT](LICENSE)