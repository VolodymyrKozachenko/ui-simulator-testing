from support.assertions_errors import AssertionsErrors


class Assertions:
    @staticmethod
    def assert_equal(expected_text, actual_text):
        assert actual_text == expected_text, AssertionsErrors.ERROR_EQUAL.format(expected_text, actual_text)

