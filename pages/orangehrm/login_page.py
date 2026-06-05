"""Page object for the OrangeHRM login screen."""

from playwright.sync_api import Page
from pages.orangehrm.dashboard_page import DashboardPage
from config import orangehrm as cfg

class LoginPage:
    """The OrangeHRM login page.

    Wraps the credential form and its error elements,
    a successful log in returns a DashboardPage class.
    """
    def __init__(self, page: Page) -> None:
        self.page = page
        self.username_input = page.locator('input[name="username"]')
        self.password_input = page.locator('input[name="password"]')
        self.login_button = page.locator('button[type="submit"]')
        self.error_alert = page.locator(".oxd-alert-content-text")
        self.field_errors = page.locator(".oxd-input-field-error-message")

    def navigate(self):
        """Navigate to the login page"""
        self.page.goto(f"{cfg.LOGIN_URL}")

    def log_in(self, username: str, password: str) -> DashboardPage:
        """Returns DashboardPage object to be able to work with it further"""
        self.username_input.fill(username)
        self.password_input.fill(password)
        self.login_button.click()
        return DashboardPage(self.page)

    def submit(self) -> None:
        """Click Submit button"""
        self.login_button.click()

    def get_error_message(self) -> str:
        """Returns the alert banner text"""
        self.error_alert.wait_for()
        return self.error_alert.inner_text()

    def get_field_errors(self) -> list[str]:
        """Returns the inline per-field validation messages"""
        self.field_errors.first.wait_for()
        return self.field_errors.all_inner_texts()
