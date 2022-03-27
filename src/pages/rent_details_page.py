import re
from datetime import datetime

from src.pages.base_page import BasePage
from src.pages.locators.rent_details_locators import RentDetailsLocators


class RentDetailsPage(BasePage):

    @staticmethod
    def _process_date(raw_date: str) -> str:
        raw_pickup_date = re.search(r": ([\w-]+)$", raw_date).group(1)
        pickup_date = datetime.strptime(raw_pickup_date, "%Y-%m-%d")
        return pickup_date.strftime("%m/%d/%Y")

    @staticmethod
    def _extract_text(raw_text: str) -> str:
        return re.search(r": ([\w\s,\-\$]+)$", raw_text).group(1)

    @classmethod
    def get_country(cls):
        raw_location_text = RentDetailsLocators.location_text().text
        return re.search(r": ([\w\s]+),", raw_location_text).group(1)

    @classmethod
    def get_city(cls):
        raw_location_text = RentDetailsLocators.location_text().text
        return re.search(r", ([\w\s]+)$", raw_location_text).group(1)

    @classmethod
    def get_pickup_date(cls):
        return cls._process_date(RentDetailsLocators.pickup_date().text)

    @classmethod
    def get_dropoff_date(cls):
        return cls._process_date(RentDetailsLocators.dropoff_date().text)

    @classmethod
    def get_rent_company(cls):
        return cls._extract_text(RentDetailsLocators.rent_company_text().text)

    @classmethod
    def get_car_model(cls):
        return RentDetailsLocators.car_model_text().text.strip()

    @classmethod
    def get_license_plate(cls):
        return cls._extract_text(RentDetailsLocators.license_plate_text().text)

    @classmethod
    def get_rent_price_per_day(cls):
        return cls._extract_text(RentDetailsLocators.rent_price_text().text)

    @classmethod
    def verify_rent(cls):
        RentDetailsLocators.verify_rent_button().click()
