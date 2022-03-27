from config import main_page_url
from src.pages.base_page import BasePage
from src.pages.main_page import MainPage
from src.utilities.utilities import Utilities


class CarRentController:

    @classmethod
    def go_to_main_page(cls):
        BasePage.driver.get(main_page_url)

    @classmethod
    def search_car(cls, country: str = None, city: str = None, car_model: str = None, pickup_date: str = None, dropoff_date: str = None):

        if not country:
            country = Utilities.pick_a_country()

        if not city:
            city = Utilities.pick_a_city(country)

        if not car_model:
            car_model = Utilities.pick_a_car_model()

        if not pickup_date:
            pickup_date = Utilities.get_current_date()

        if not dropoff_date:
            dropoff_date = Utilities.get_delayed_date(1)

        MainPage.select_country(country)
        MainPage.select_city(city)
        MainPage.select_car_model(car_model)
        MainPage.select_pickup_date(pickup_date)
        MainPage.select_dropoff_date(dropoff_date)
        MainPage.search_car()
