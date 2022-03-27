from selenium.webdriver.common.by import By
from src.pages.base_page import BasePage
from src.pages.locators.locator_decorators import get_element


class MainPageLocators(BasePage):

    @classmethod
    @get_element
    def country_dropdown(cls):
        return By.ID, "country"

    @classmethod
    @get_element
    def city_dropdown(cls):
        return By.ID, "city"

    @classmethod
    @get_element
    def car_model_field(cls):
        return By.ID, "model"

    @classmethod
    @get_element
    def pickup_date_field(cls):
        return By.ID, "pickup"

    @classmethod
    @get_element
    def dropoff_date_field(cls):
        return By.ID, "dropoff"

    @classmethod
    @get_element
    def search_button(cls):
        return By.XPATH, "//button[text()='Search']"

    @classmethod
    @get_element
    def rent_button(cls):
        return By.XPATH, "//a[text()='Rent']"
