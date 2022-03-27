import datetime
import random

from src.data.constants.available_countries import AvailableCountries
from src.data.constants.car_models import CarModels


class Utilities:

    @staticmethod
    def pick_a_country():
        return random.choice(list(AvailableCountries)).name.capitalize()

    @staticmethod
    def pick_a_city(country: str):
        country_cities = list(filter(lambda available_country: available_country.name.capitalize() == country.capitalize(), AvailableCountries))[0].value
        return random.choice(country_cities)

    @staticmethod
    def pick_a_car_model():
        return random.choice(list(CarModels)).value.capitalize()

    @staticmethod
    def get_current_date():
        return datetime.date.today().strftime("%m/%d/%Y")

    @staticmethod
    def get_delayed_date(amount_days: int):
        return (datetime.date.today() + datetime.timedelta(amount_days)).strftime("%m/%d/%Y")
