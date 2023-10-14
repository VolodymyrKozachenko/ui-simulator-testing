import pytest
import allure

case_1 = ["", "correct_password", "Username field cannot be empty"]
case_2 = ["correct_username", "", "Password field cannot be empty"]
case_3 = ["incorrect_username", "correct_password", "Password or username is incorrect"]
case_4 = ["correct_username", "incorrect_password", "Password or username is incorrect"]

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
    index_page.enter_username("correct_username")
    index_page.enter_password("correct_password")
    index_page.click_to_login_button()
    index_page.validate_login()
