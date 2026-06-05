import pytest

from pages.orangehrm.dashboard_page import DashboardPage


class TestDashboard:

    @pytest.mark.smoke
    def test_authenticate_with_cookies(self, logged_in_context):
        page = logged_in_context.new_page()
        dashboard = DashboardPage(page)
        dashboard.navigate()
        assert "dashboard/index" in dashboard.page.url

    def test_navigate_to_admin(self, logged_in_context):
        page = logged_in_context.new_page()
        dashboard = DashboardPage(page)
        dashboard.navigate_to_admin()
        assert "admin/viewSystemUsers" in dashboard.page.url
