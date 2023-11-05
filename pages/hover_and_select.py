from selenium.webdriver.common.by import By
from base_object.base import BaseObject
from support.assertions import Assertions


class HoverAndSelect(BaseObject, Assertions):

    SELECT_TEXT = (By.XPATH, "/html/body/div[2]/div/div[1]")
    DRAG_AND_DROP = (By.XPATH, "/html/body/div[2]/div/div[2]/ul/li[1]/a")
    INPUT_AND_CLICK = (By.XPATH, "/html/body/div[2]/div/div[2]/ul/li[2]/a")
    CHECKBOX_AND_SCROLL = (By.XPATH, "/html/body/div[2]/div/div[2]/ul/li[3]/a")
    CHECK_AND_VALIDATE = (By.XPATH, "/html/body/div[2]/div/div[2]/ul/li[4]/a")
    SORT_BY = (By.XPATH, "/html/body/div[2]/div/div[2]/ul/li[5]/a")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def hover_on_button(self):
        self.hover(self.SELECT_TEXT)

    def select_element(self, locator):
        pass
