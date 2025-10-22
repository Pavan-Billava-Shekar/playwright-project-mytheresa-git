from pages.login_page import LoginPage

def test_user_can_login(page, base_url, credentials):
    """
    Test: Verify that a user can log in successfully.
    This uses Page Object Model and data from YAML.
    """
    login_page = LoginPage(page)

    # Step 1: Navigate to login page
    login_page.navigate(base_url)

    # Step 2: Perform login
    login_page.login(credentials["username"], credentials["password"])

    # Step 3: Verify login success
    login_page.verify_login_success()
