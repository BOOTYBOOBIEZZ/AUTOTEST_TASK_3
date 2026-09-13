import pytest
from playwright.sync_api import Browser

from logger import setup_logger


@pytest.fixture(scope="session", autouse=True)
def init_logger():
    setup_logger()


@pytest.fixture
def authenticated_context(browser: Browser):
    context = browser.new_context(
        http_credentials={"username": "admin", "password": "admin"}
    )
    yield context
    context.close()


@pytest.fixture
def page(authenticated_context):
    """Страница с авторизацией."""
    page = authenticated_context.new_page()
    yield page
    page.close()


@pytest.fixture
def user_1():
    return
