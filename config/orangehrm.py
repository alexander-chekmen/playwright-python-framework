"""OrangeHRM environment configuration.

Resolves the base URL and derived dashboard URLs from environment
variables, falling back to the public demo site so the suite runs out of the
box.
"""
import os

BASE_URL = os.getenv(
    "ORANGEHRM_BASE_URL",
    "https://opensource-demo.orangehrmlive.com/web/index.php",
)

LOGIN_URL     = f"{BASE_URL}/auth/login"
DASHBOARD_URL = f"{BASE_URL}/dashboard/index"
ADMIN_URL     = f"{BASE_URL}/admin/viewSystemUsers"
PIM_URL       = f"{BASE_URL}/pim/viewEmployeeList"
LEAVE_URL     = f"{BASE_URL}/leave/viewLeaveList"
TIME_URL      = f"{BASE_URL}/time/viewEmployeeTimesheet"