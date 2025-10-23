import pytest
import yaml
from pathlib import Path
from playwright.sync_api import sync_playwright

CONFIG_PATH = Path(__file__).parent / "config" / "config.yaml"


def load_config():
    """Load configuration from the YAML file."""
    with open(CONFIG_PATH, "r", encoding="utf-8") as f:
        return yaml.safe_load(f)


@pytest.fixture(scope="session")
def config():
    """Provide configuration data for the entire test session."""
    return load_config()


def pytest_addoption(parser):
    """Add CLI options for dynamic environment and browser selection."""
    parser.addoption("--env", action="store", default=None, help="Environment: local/staging/production")
    # ✅ renamed to avoid conflict with pytest-playwright
    parser.addoption("--browser_name", action="store", default=None, help="Browser: chromium/firefox/webkit")


@pytest.fixture(scope="session")
def base_url(config, request):
    """Select the correct base URL based on the environment flag or default."""
    env = request.config.getoption("--env") or config["default"]["environment"]
    return config["environments"][env]["base_url"]


@pytest.fixture(scope="session")
def browser_type(config, request):
    """Select browser type dynamically."""
    return request.config.getoption("--browser_name") or config["default"]["browser"]


@pytest.fixture(scope="session")
def credentials(config):
    """Provide credentials to the test suite."""
    return config["credentials"]


@pytest.fixture(scope="session")
def browser_context(browser_type):
    """Launch Playwright and return a reusable browser context."""
    with sync_playwright() as playwright:
        browser = getattr(playwright, browser_type).launch(headless=True)
        context = browser.new_context()
        yield context
        context.close()
        browser.close()


@pytest.fixture()
def page(browser_context):
    """Provide a fresh page instance for each test."""
    page = browser_context.new_page()
    yield page
    page.close()

@pytest.fixture(scope="session")
def repo_url(config, request):
    """Select the repo URL from config."""
    env = request.config.getoption("--env") or config["default"]["environment"]
    return config["environments"][env]["repo_url"]

@pytest.fixture(scope="session")
def repo_list(config):
    with open(CONFIG_PATH, "r") as file:
        data = yaml.safe_load(file)
    return data["repositories"]