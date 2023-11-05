from selenium import webdriver
from selenium.webdriver.chrome.options import Options as ChromeOptions
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.index_page import IndexPage
from pages.input_and_click_page import InputAndClickPage
from pages.check_and_validate_page import CheckAndValidatePage
from pages.hover_and_select import HoverAndSelect
import pytest
from env_setup import ROOT_PATH
import os


@pytest.fixture
def get_webdriver():
    options = ChromeOptions()
    options.add_argument('--start-maximized')
    driver = webdriver.Chrome(options=options, service=Service(ChromeDriverManager().install()))
    return driver


@pytest.fixture
def index_page(get_webdriver):
    get_webdriver.get("https://toghrulmirzayev.github.io/ui-simulator/")
    yield IndexPage(get_webdriver)
    get_webdriver.quit()


@pytest.fixture
def input_and_click_page(get_webdriver):
    get_webdriver.get("https://toghrulmirzayev.github.io/ui-simulator/input-and-click.html")
    yield InputAndClickPage(get_webdriver)
    get_webdriver.quit()


@pytest.fixture
def check_and_validate_page(get_webdriver):
    get_webdriver.get("https://toghrulmirzayev.github.io/ui-simulator/check_and_validate.html")
    yield CheckAndValidatePage(get_webdriver)
    get_webdriver.quit()


@pytest.fixture
def hover_and_select(get_webdriver):
    get_webdriver.get("https://toghrulmirzayev.github.io/ui-simulator/hover_and_select.html")
    yield HoverAndSelect(get_webdriver)
    get_webdriver.quit()


@pytest.fixture(scope='function', autouse=True)
def screenshot_on_failures(get_webdriver, request):
    failed_tests_count = request.session.testsfailed
    yield
    if request.session.testsfailed > failed_tests_count:
        test_case_name = request.node.name
        screenshot = os.path.join(ROOT_PATH, f"screenshot_on_failures_{test_case_name}.png")
        get_webdriver.get_screenshot_as_file(screenshot)
