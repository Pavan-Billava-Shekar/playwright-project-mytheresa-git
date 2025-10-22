from playwright.sync_api import Page, expect

class LoginPage:
    """Page Object Model for the FashionHub login page."""

    def __init__(self, page: Page):
        self.page = page
        # Element locators (kept internal)
        self.username_field = "#username"
        self.password_field = "#password"
        # self.login_button = "button[type='submit']"
        self.success_indicator = "text=Welcome, testUser!"  # Adjust as needed for your UI

    def navigate(self, base_url: str):
        """Navigate to the login page."""
        self.page.goto(f"{base_url}login.html")

    def login(self, username: str, password: str):
        """Perform login with provided credentials."""
        self.page.fill(self.username_field, username)
        self.page.fill(self.password_field, password)
        self.page.get_by_role("button", name="Login").click()

    def verify_login_success(self):
        """Verify that the login was successful."""
        expect(self.page.locator(self.success_indicator)).to_be_visible()
