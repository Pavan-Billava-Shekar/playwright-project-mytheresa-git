from pages.home_page import HomePage

def test_links_status_code(page, base_url):
    """check that all the links of home page returns valid status code"""
    home = HomePage(page, base_url)
    home.goto()
    passed_links, failed_links = home.check_links_status() # get passed and failed links
    if passed_links:
        print("Passed links:")
        for link in passed_links:
            print(link)
    assert not failed_links, f"Some links failed: {failed_links}" # failed links