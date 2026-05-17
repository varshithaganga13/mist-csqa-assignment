import pytest
from libs.ui_libs.todo_create_account_libs import CreateAccountLibs
from utils.ui_utils.ui_utils import UIUtils


class TestCreateAccount:
    """
    Test class for Create Account page UI automation.
    Tests navigation, page load, and account creation form submission.
    """

    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        """Setup WebDriver before each test and quit after."""
        self.driver = UIUtils.get_driver()
        self.create_account = CreateAccountLibs(self.driver)
        yield
        if hasattr(self, 'driver') and self.driver:
            self.driver.quit()

    def test_navigate_to_create_account(self):
        """Test that navigating to the create account page loads the correct URL."""
        self.create_account.navigate_to_create_account_page()
        assert "signup/register" in self.driver.current_url

    def test_page_title(self):
        """Test that the page title is present after navigation."""
        self.create_account.navigate_to_create_account_page()
        assert self.driver.title, "Page title is empty"

    def test_create_account(self):
        """
        Test the full create account flow:
        a) Navigate to the registration page
        b) Enter details for the form fields
        c) Click the Create Account button
        Note: CAPTCHA may be triggered after clicking — this is expected.
        """
        self.create_account.navigate_to_create_account_page()

        self.create_account.enter_first_name("Test")
        self.create_account.enter_last_name("User")
        self.create_account.enter_email("testuser@example.com")
        self.create_account.enter_password("SecurePass123!")
        self.create_account.click_create_account()