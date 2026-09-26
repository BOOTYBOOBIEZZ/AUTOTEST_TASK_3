import pytest
from playwright.sync_api import Browser, Page

from logger import setup_logger
from pages.alerts_page import AlertsPage
from pages.context_click_page import ContextClickPage
from pages.download_page import DownloadPage
from pages.dynamic_content_page import DynamicContentPage
from pages.frames_page import FramesPage
from pages.horizontal_slider_page import HorizontalSliderPage
from pages.hovers_page import HoversPage
from pages.login_page import LoginPage
from pages.new_window_page import NewWindowPage
from pages.scroll_page import ScrollPage
from pages.upload_image_page import UploadPage
from utils.url_utils import (
    ALERTS_URL,
    CONTEXT_MENU_URL,
    DOWNLOAD_URL,
    DYNAMIC_CONTENT_URL,
    FRAMES_URL,
    HORIZONTAL_URL,
    HOVERS_URL,
    LOGIN_URL,
    NEW_WINDOW_URL,
    SCROLL_URL,
    UPLOAD_URL,
)


@pytest.fixture
def alerts_page(page: Page) -> AlertsPage:
    page.goto(ALERTS_URL)
    return AlertsPage(page)


@pytest.fixture
def context_click_page(page: Page) -> ContextClickPage:
    page.goto(CONTEXT_MENU_URL)
    return ContextClickPage(page)


@pytest.fixture
def download_page(page: Page) -> DownloadPage:
    page.goto(DOWNLOAD_URL)
    return DownloadPage(page)


def dynamic_content_page(page: Page) -> DynamicContentPage:
    page.goto(DYNAMIC_CONTENT_URL)
    return DynamicContentPage(page)


@pytest.fixture
def frames_page(page: Page) -> FramesPage:
    page.goto(FRAMES_URL)
    return FramesPage(page)


@pytest.fixture
def horizontal_slider_page(page: Page) -> HorizontalSliderPage:
    page.goto(HORIZONTAL_URL)
    return HorizontalSliderPage(page)


@pytest.fixture
def hovers_page(page: Page) -> HoversPage:
    page.goto(HOVERS_URL)
    return HoversPage(page)


@pytest.fixture
def login_page(page: Page) -> LoginPage:
    page.goto(LOGIN_URL)
    return LoginPage(page)


@pytest.fixture
def upload_image_page(page: Page) -> UploadPage:
    page.goto(UPLOAD_URL)
    return UploadPage(page)


@pytest.fixture
def new_window_page(page: Page) -> NewWindowPage:
    page.goto(NEW_WINDOW_URL)
    return NewWindowPage(page)


@pytest.fixture
def scroll_page(page: Page) -> ScrollPage:
    page.goto(SCROLL_URL)
    return ScrollPage(page)


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
