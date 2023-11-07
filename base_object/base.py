"""
Base Object for base method
"""
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.ui import WebDriverWait
from support.logger import log_func
from typing import List
from selenium.webdriver import ActionChains
from selenium.webdriver.support.select import Select
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.remote.webelement import WebElement


class BaseObject:

    LOG = log_func()

    def __init__(self, driver: WebDriver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 5)

    def is_visible(self, locator) -> WebElement:
        self.LOG.info(f'Element {locator} is visible')
        return self.wait.until(ec.visibility_of_element_located(locator))

    def are_visible(self, locator) -> List[WebElement]:
        return self.wait.until(ec.visibility_of_all_elements_located(locator))

    def is_clickable(self, locator) -> WebElement:
        self.LOG.info(f'Element {locator} is clickable')
        return self.wait.until(ec.element_to_be_clickable(locator))

    def click(self, locator: tuple) -> None:
        """
        Method to click
        :param locator: locator for click
        :return: None
        """
        self.LOG.info(f'Element {locator} is click')
        self.is_clickable(locator).click()

    def send_keys(self, locator, data):
        self.LOG.info(f'Send keys {data} to Element {locator}')
        self.is_visible(locator).send_keys(data)

    def get_text(self, locator) -> str:
        self.LOG.info(f'Received text with Element {locator}')
        return self.is_visible(locator).text

    def hover(self, locator):
        mouse = ActionChains(self.driver)
        elem = self.is_visible(locator)
        mouse.move_to_element(elem).perform()

    def drag_and_drop(self, locator1, locator2):
        actions = ActionChains(self.driver)
        to_drag_elem = self.is_visible(locator1)
        to_drop_elem = self.is_visible(locator2)
        actions.drag_and_drop(to_drag_elem, to_drop_elem).perform()

    def get_attribute_of_elements(self, locator, data):
        image_element = self.is_visible(locator)
        actual_text = image_element.get_attribute(data)
        print(actual_text)

    def css_property(self, locator, data_of_colour):
        elem = self.is_visible(locator)
        color = elem.value_of_css_property(data_of_colour)
        expected_color = ''
        assert expected_color == color

    def select_class(self, locator, list_item):
        dropdown = self.is_visible(locator)
        select = Select(dropdown)
        select.select_by_visible_text(list_item)
