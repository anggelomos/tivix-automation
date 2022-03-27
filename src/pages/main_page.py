import random

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from src.data.constants.car_data_fields import CarDataFields
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
    def enter_car_model(cls, car_model):
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

    @classmethod
    def select_car(cls):
        car_list = MainPageLocators.car_list()
        raw_car_web_elements = random.choice(car_list).find_elements(By.TAG_NAME, "td")

        raw_car_data = list(map(lambda car_field: car_field.text, raw_car_web_elements))[:-1]
        car_data_fields = list(map(lambda field: field.value, CarDataFields))
        car_data = dict(zip(car_data_fields, raw_car_data))

        raw_car_web_elements[-1].click()
        return car_data
