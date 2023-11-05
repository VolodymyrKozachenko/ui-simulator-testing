import pytest
import allure

def test_select_elements(hover_and_select):
    hover_and_select.hover_on_button()
    hover_and_select.select_elements()


