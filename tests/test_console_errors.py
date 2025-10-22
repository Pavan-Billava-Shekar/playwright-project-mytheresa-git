import pytest
from pages.home_page_error import HomePageError


def test_console_errors(page, base_url, credentials):
    """
    This testcase ensures that visiting each URL does not produce console errors.
    """
    url = base_url
    base_page = HomePageError(page)
    base_page.navigate(url)
    errors = base_page.get_console_errors()
    if errors:
        pytest.fail(f"Console errors found on {url}:\n" + "\n".join(errors))
    else:
        pass
