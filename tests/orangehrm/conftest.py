"""Fixtures scoped to the OrangeHRM suite."""
import pytest
from pages.orangehrm.login_page import LoginPage
from config import orangehrm as cfg

@pytest.fixture
def login_page(page):
    """Navigate to login page and return LoginPage object"""
    lp = LoginPage(page)
    lp.navigate()
    return lp

@pytest.fixture(scope='session')
def credentials(browser):
    """Fetches login credentials once per session from the login page"""
    context = browser.new_context()
    page = context.new_page()
    page.goto(cfg.LOGIN_URL)
    el1 = page.locator("//*[@id='app']//p").nth(0).text_content()
    el2 = page.locator("//*[@id='app']//p").nth(1).text_content()
    context.close()
    return {
        "username": el1.split(':')[1].strip(' '),
        "password": el2.split(':')[1].strip(' ')
    }

@pytest.fixture(scope="session")
def auth_storage(browser, credentials):
    """Logs in once per session and saves storage state to state.json"""
    context = browser.new_context()
    page = context.new_page()

    lp = LoginPage(page)
    lp.navigate()
    lp.log_in(credentials["username"], credentials["password"])
    page.wait_for_url("**/dashboard/**")
    context.storage_state(path="state.json")

    yield "state.json"

    context.close()

@pytest.fixture
def logged_in_context(browser, auth_storage):

    context = browser.new_context(
        storage_state=auth_storage
    )

    yield context

    context.close()


