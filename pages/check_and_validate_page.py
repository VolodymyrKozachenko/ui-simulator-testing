from selenium.webdriver.common.by import By
from base_object.base import BaseObject


class CheckAndValidatePage(BaseObject):

    VALUE_FIELD = (By.ID, "dataInput")
    VALUE_DISPLAY = (By.ID, "validationSquare")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_data(self, data):
        self.send_keys(self.VALUE_FIELD, data)

    def validate_message(self, validate_message):
        expected_text = validate_message
        actual_text = self.get_text(self.VALUE_DISPLAY)
        assert actual_text == expected_text, f"FAILED. Expected {expected_text}, but actually got {actual_text}"
