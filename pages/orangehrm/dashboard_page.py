"""Page object for the OrangeHRM dashboard (post-login landing page)."""
from playwright.sync_api import Page
from config import orangehrm as cfg

class DashboardPage:

    def __init__(self, page: Page):
        self.page = page
        self.user_dropdown = page.locator(".oxd-userdropdown-name")
        self.logout_menu_item = page.get_by_role("menuitem", name="Logout")

    def navigate(self):
        """Go straight to the dashboard URL (used for access-control tests)."""
        self.page.goto(cfg.DASHBOARD_URL)

    def navigate_to_admin(self):
        """Go straight to the admin URL (used for access-control tests)."""
        self.page.goto(cfg.ADMIN_URL)

    def logout(self):
        """Open the user menu and log out.

        Returns the Playwright Page object so callers can assert the
        post-logout URL (the app redirects to the login screen).
        """
        self.user_dropdown.click()
        self.logout_menu_item.click()
        return self.page