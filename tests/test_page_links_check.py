from pages.home_page import HomePage

def test_links_status_code(page, base_url):
    """Check all links on the home page for valid status codes."""
    home = HomePage(page, base_url)
    home.goto()
    passed_links, failed_links = home.check_links_status()

    if passed_links:
        print("Passed links:")
        for link in passed_links:
            print(link)

    # Assert no failed links
    assert not failed_links, f"Some links failed: {failed_links}"
