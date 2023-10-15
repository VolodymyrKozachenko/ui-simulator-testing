import pytest

case_1 = [11, "Valid"]
case_2 = [9, "Not in range"]
case_3 = [11.5, "Not an integer"]
case_4 = [-11, "Negative integer"]
case_5 = [-11.5, "Negative number"]
case_6 = ["hello", "Not a number"]


@pytest.mark.smoke
@pytest.mark.parametrize("data, validate_message", (case_1, case_2, case_3, case_4, case_5, case_6))
def test_data_validation(check_and_validate_page, data, validate_message):
    check_and_validate_page.enter_data(data)
    check_and_validate_page.validate_message(validate_message)

