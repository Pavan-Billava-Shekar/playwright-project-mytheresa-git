import pytest
from pages.home_page_error import HomePageError

def test_console_errors(page, base_url, credentials):
    """Check if there are any console error in the given URL"""
    url = base_url
    base_page = HomePageError(page)
    base_page.navigate(url)
    errors = base_page.get_console_errors()
    if errors:
        pytest.fail(f"Console errors found on {url}:\n" + "\n".join(errors))
    else:
        pass
