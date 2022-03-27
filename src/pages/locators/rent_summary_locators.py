from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.pages.locators.locator_decorators import get_element, get_elements


class RentSummaryLocators(BasePage):

    @classmethod
    @get_element
    def name_input(cls):
        return By.ID, "name"

    @classmethod
    @get_element
    def last_name_input(cls):
        return By.ID, "last_name"

    @classmethod
    @get_element
    def card_number_input(cls):
        return By.ID, "card_number"

    @classmethod
    @get_element
    def email_input(cls):
        return By.ID, "email"

    @classmethod
    @get_element
    def rent_button(cls):
        return By.XPATH, "//button[text()='Rent']"
