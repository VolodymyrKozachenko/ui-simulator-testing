from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from support.logger import log_func


class BaseObject:

    LOG = log_func()

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_visible(self, locator):
        self.LOG.info(f'Element {locator} is visible')
        return self.wait.until(ec.visibility_of_element_located(locator))

    def is_clickable(self, locator):
        self.LOG.info(f'Element {locator} is clickable')
        return self.wait.until(ec.element_to_be_clickable(locator))

    def click(self, locator):
        self.LOG.info(f'Element {locator} is click')
        self.is_clickable(locator).click()

    def send_keys(self, locator, data):
        self.LOG.info(f'Send keys {data} to Element {locator}')
        self.is_visible(locator).send_keys(data)

    def get_text(self, locator):
        self.LOG.info(f'Received text with Element {locator}')
        return self.is_visible(locator).text





