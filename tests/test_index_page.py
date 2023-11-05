import pytest
import allure
from env_setup import LOGIN, PASSWORD

case_1 = ["", PASSWORD, "Username field cannot be empty"]
case_2 = [LOGIN, "", "Password field cannot be empty"]
case_3 = ["incorrect_username", PASSWORD, "Password or username is incorrect"]
case_4 = [LOGIN, "incorrect_password", "Password or username is incorrect"]

@pytest.mark.smoke
@pytest.mark.parametrize("data_login, data_password, error_message", (case_1, case_2, case_3, case_4))
def test_login_error_message(index_page, data_login, data_password, error_message):
    index_page.enter_username(data_login)
    index_page.enter_password(data_password)
    index_page.click_to_login_button()
    index_page.validate_error_message(error_message)


@allure.description('success login with correct creds')
@allure.label('owner', 'Vova')
@allure.title('success login')
@allure.suite('Auhtorization')
@allure.severity(allure.severity_level.BLOCKER)
def test_success_login(index_page):
    index_page.enter_username(LOGIN)
    index_page.enter_password(PASSWORD)
    index_page.click_to_login_button()
    index_page.validate_login()
