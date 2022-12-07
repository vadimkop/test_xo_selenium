from .base_page import BasePage
from .locators import SearchLocators, LoginLocators
import pytest_check as check
from faker import Faker

fake = Faker()


class Login(BasePage):

    def incorrect_login(self):
        self.find_element(SearchLocators.PRESENT_DAY).click()
        check.is_true(self.element_displayed(*LoginLocators.MODAL_LOGIN))

        self.find_element(LoginLocators.INPUT_EMAIL).send_keys(fake.email())
        self.find_element(LoginLocators.INPUT_PASSWORD).send_keys(fake.password())
        self.find_element(LoginLocators.BUTTON_LOGIN).click()
        check.is_in("Please try again", self.find_element(LoginLocators.LOGIN_ERROR).text)


