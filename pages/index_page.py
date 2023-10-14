from selenium.webdriver.common.by import By
from base_object.base import BaseObject
from support.assertions import Assertions


class IndexPage(BaseObject, Assertions):

    USERNAME_FIELD = (By.ID, "username")
    PASSWORD_FIELD = (By.ID, "password")
    LOGIN_BTN = (By.CLASS_NAME, "login-button")
    LOGOUT_BTN = (By.CLASS_NAME, "logout-button")
    ERROR_MESSAGE = (By.ID, "message")

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    def enter_username(self, data_login):
        self.send_keys(self.USERNAME_FIELD, data_login)

    def enter_password(self, data_password):
        self.send_keys(self.PASSWORD_FIELD, data_password)

    def click_to_login_button(self):
        self.click(self.LOGIN_BTN)

    def validate_login(self):
        self.assert_equal("Log out", self.get_text(self.LOGOUT_BTN))

    def validate_error_message(self, error_message):
        self.assert_equal(error_message, self.get_text(self.ERROR_MESSAGE))
