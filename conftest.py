import pytest
import yaml
from pathlib import Path
from playwright.sync_api import sync_playwright

CONFIG_PATH = Path(__file__).parent / "config" / "config.yaml"


def load_config():
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:  # Load configuration from the YAML file
        return yaml.safe_load(f)


@pytest.fixture(scope="session")
def config():
    return load_config() #Provide configuration data


def pytest_addoption(parser):
    parser.addoption("--env", action="store", default=None, help="Environment: local/staging/production")
    parser.addoption("--browser_name", action="store", default=None, help="Browser: chromium/firefox/webkit")


@pytest.fixture(scope="session")
def base_url(config, request):
    #base URL and Environment selection
    env = request.config.getoption("--env") or config["default"]["environment"]
    return config["environments"][env]["base_url"]


@pytest.fixture(scope="session")
def browser_type(config, request):
  #browser selection
    return request.config.getoption("--browser_name") or config["default"]["browser"]


@pytest.fixture(scope="session")
def credentials(config):
# cred selection
    return config["credentials"]


@pytest.fixture(scope="session")
def browser_context(browser_type):
    with sync_playwright() as playwright: #browser instant
        browser = getattr(playwright, browser_type).launch(headless=True)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


@pytest.fixture()
def page(browser_context):
    page = browser_context.new_page() #page instant
    yield page
    page.close()

page_urls_list = [
    {"url": "https://pocketaces2.github.io/fashionhub/"},
    {"url": "https://pocketaces2.github.io/fashionhub/about.html"}  # intentional error
]

REPO_URL = "https://github.com/appwrite/appwrite/pulls"


@pytest.fixture(scope="session")
def repo_url(config, request):  #repourl selection
    env = request.config.getoption("--env") or config["default"]["environment"]
    return config["environments"][env]["repo_url"]