import pytest
from config import orangehrm as cfg


class TestAuthentication:
    """Login, logout, field validation and access-control scenarios."""

    @pytest.mark.smoke
    def test_successful_login_valid_credentials(self, login_page, credentials):
        login_page.log_in(credentials["username"], credentials["password"])
        login_page.page.wait_for_url("**/dashboard/**")
        assert "dashboard" in login_page.page.url

    def test_login_using_enter_key(self, login_page, credentials):
        """Providing username, password and simulating pressing 'Enter' button on keyboard"""
        login_page.username_input.fill(credentials["username"])
        login_page.password_input.fill(credentials["password"])
        login_page.page.keyboard.press("Enter")
        login_page.page.wait_for_url("**/dashboard/**")
        assert "dashboard" in login_page.page.url

    def test_login_fails_with_invalid_password(self, login_page, credentials):
        login_page.username_input.fill(credentials["username"])
        login_page.password_input.fill("invalidPwd")
        login_page.submit()
        assert login_page.get_error_message() == 'Invalid credentials'

    def test_login_fails_with_invalid_username(self, login_page, credentials):
        login_page.username_input.fill("invalidUser")
        login_page.password_input.fill(credentials["password"])
        login_page.submit()
        assert login_page.get_error_message() == 'Invalid credentials'

    def test_login_fails_with_empty_username(self, login_page, credentials):
        login_page.password_input.fill(credentials["password"])
        login_page.submit()
        errors = login_page.get_field_errors()
        assert len(errors) == 1
        assert "Required" in errors

    def test_login_fails_with_empty_password(self, login_page, credentials):
        login_page.username_input.fill(credentials["username"])
        login_page.submit()
        errors = login_page.get_field_errors()
        assert len(errors) == 1
        assert "Required" in errors

    def test_empty_form_shows_required_fields(self, login_page):
        login_page.submit()
        errors = login_page.get_field_errors()
        assert len(errors) == 2
        assert all("Required" in e for e in errors)

    def test_password_field_masks_input(self, login_page):
        password_type = login_page.password_input.get_attribute("type")
        assert password_type == "password"

    def test_logout(self, login_page, credentials):
        dashboard_page = login_page.log_in(credentials["username"], credentials["password"])
        dashboard_page.logout()
        dashboard_page.page.wait_for_url("**/auth/login**")
        assert 'auth/login' in dashboard_page.page.url

    def test_access_protected_page_after_logout(self, login_page, credentials):
        """After logout, re-requesting the dashboard URL redirects to login."""
        dashboard_page = login_page.log_in(credentials["username"], credentials["password"])
        dashboard_page.logout()
        dashboard_page.page.goto(cfg.DASHBOARD_URL)
        # assert that when trying to get to the dashboard URL, the system redirects to login
        assert '/auth/login' in dashboard_page.page.url

    def test_unauthenticated_user_cannot_access_dashboard(self, login_page):
        """Verify that access to the Dashboard is blocked for unauthenticated users
        and they are redirected to the login page.
        """
        login_page.page.goto(cfg.DASHBOARD_URL)
        assert "/auth/login" in login_page.page.url

    def test_forgot_password_navigation(self, login_page):
        """Verify the Forgot Password link navigates the user to the
        password reset page.
        """
        login_page.page.get_by_text("Forgot your password?").click()
        assert 'auth/requestPasswordResetCode' in login_page.page.url
