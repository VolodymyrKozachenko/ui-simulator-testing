from selenium.webdriver.common.by import By
from base_object.base import BaseObject


class InputAndClickPage(BaseObject):

    DATA_FIELD = (By.ID, "inputText")
    ITEMS_FIELD = (By.ID, "items")
    ADD_BTN = (By.ID, "addBtn")
    DELETE_BTN = (By.ID, "deleteBtn")
    BACK_BTN = (By.CLASS_NAME, "back-button")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_data(self, any_data):
        self.send_keys(self.DATA_FIELD, any_data)

    def click_to_add_button(self):
        self.click(self.ADD_BTN)

    def valid_data(self):
        expected_text = "hello"
        actual_text = self.get_text(self.ITEMS_FIELD)
        assert actual_text == expected_text, f"FAILED. Expected {expected_text}, but actually got {actual_text}"



