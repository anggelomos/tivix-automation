from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.pages.locators.locator_decorators import get_element, get_elements


class RentDetailsLocators(BasePage):

    @staticmethod
    def _generic_card_text(text: str) -> str:
        return f"//*[contains(@class, 'card') and contains(text(), '{text}')]"

    @staticmethod
    def _generic_h6(text: str):
        return f"//h6[contains(text(), '{text}')]"

    @classmethod
    @get_element
    def country_dropdown(cls):
        return By.ID, "country"

    @classmethod
    @get_element
    def location_text(cls):
        return By.XPATH, cls._generic_card_text("Location")

    @classmethod
    @get_element
    def pickup_date(cls):
        return By.XPATH, cls._generic_h6("Pickup")

    @classmethod
    @get_element
    def dropoff_date(cls):
        return By.XPATH, cls._generic_h6("Dropoff")

    @classmethod
    @get_element
    def rent_company_text(cls):
        return By.XPATH, cls._generic_card_text("Company")

    @classmethod
    @get_element
    def car_model_text(cls):
        return By.CSS_SELECTOR, ".card-header"

    @classmethod
    @get_element
    def license_plate_text(cls):
        return By.XPATH, cls._generic_card_text("License")

    @classmethod
    @get_element
    def rent_price_text(cls):
        return By.XPATH, cls._generic_card_text("Price")

    @classmethod
    @get_element
    def verify_rent_button(cls):
        return By.XPATH, "//a[contains(text(), 'Rent')]"
