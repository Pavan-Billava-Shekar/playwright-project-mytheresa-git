from pages.login_page import LoginPage

def test_user_can_login(page, base_url, credentials):
    """
    This  testcase ensures user is able to Verify that a user can log in successfully.    """
    login_page = LoginPage(page)    # Navigate to login page
    login_page.navigate(base_url)
    login_page.login(credentials["username"], credentials["password"])  # login via yaml cred
    login_page.verify_login_success()   #check login success
