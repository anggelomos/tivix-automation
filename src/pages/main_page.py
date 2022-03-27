from selenium.webdriver.support.select import Select
from src.pages.base_page import BasePage
from src.pages.locators.main_page_locators import MainPageLocators


class MainPage(BasePage):

    @classmethod
    def select_country(cls, country):
        Select(MainPageLocators.country_dropdown()).select_by_visible_text(country)

    @classmethod
    def select_city(cls, city):
        Select(MainPageLocators.city_dropdown()).select_by_visible_text(city)

    @classmethod
    def select_car_model(cls, car_model):
        MainPageLocators.car_model_field().send_keys(car_model)

    @classmethod
    def select_pickup_date(cls, pickup_date):
        MainPageLocators.pickup_date_field().send_keys(pickup_date)

    @classmethod
    def select_dropoff_date(cls, dropoff_date):
        MainPageLocators.dropoff_date_field().send_keys(dropoff_date)

    @classmethod
    def search_car(cls):
        MainPageLocators.search_button().click()
