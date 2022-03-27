from assertpy import assert_that
from config import main_page_url
from faker.generator import random
from src.data.data_models.rent_data import RentDataModel, LocalizationDataModel, CarDataModel
from src.pages.base_page import BasePage
from src.pages.main_page import MainPage
from src.pages.rent_details_page import RentDetailsPage
from src.pages.rent_summary_page import RentSummaryPage
from src.utilities.utilities import Utilities


class CarRentController:

    rent_data = RentDataModel()

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

        cls.rent_data.localization_data = LocalizationDataModel(country=country, city=city, pickup_date=pickup_date, dropoff_date=dropoff_date)
        MainPage.select_country(country)
        MainPage.select_city(city)
        MainPage.enter_car_model(car_model)
        MainPage.select_pickup_date(pickup_date)
        MainPage.select_dropoff_date(dropoff_date)
        MainPage.search_car()

    @classmethod
    def select_car(cls):
        car_data = MainPage.select_car()
        cls.rent_data.car_data = CarDataModel(**car_data)

    @classmethod
    def verify_rent_information(cls):
        assert_that(RentDetailsPage.get_country()).is_equal_to(cls.rent_data.localization_data.country)
        assert_that(RentDetailsPage.get_city()).is_equal_to(cls.rent_data.localization_data.city)
        assert_that(RentDetailsPage.get_pickup_date()).is_equal_to(cls.rent_data.localization_data.pickup_date)
        assert_that(RentDetailsPage.get_dropoff_date()).is_equal_to(cls.rent_data.localization_data.dropoff_date)

        assert_that(RentDetailsPage.get_rent_company()).is_equal_to(cls.rent_data.car_data.rent_company)
        assert_that(RentDetailsPage.get_car_model()).is_equal_to(cls.rent_data.car_data.car_model)
        assert_that(RentDetailsPage.get_license_plate()).is_equal_to(cls.rent_data.car_data.license_plate)
        assert_that(RentDetailsPage.get_rent_price_per_day()).is_equal_to(cls.rent_data.car_data.rent_price_per_day)

        RentDetailsPage.verify_rent()

    @classmethod
    def enter_personal_data(cls, name: str = None, last_name: str = None, card_number: int = None, email: str = None):

        if not name:
            name = Utilities.generate_name()

        if not last_name:
            last_name = Utilities.generate_last_name()

        if not card_number:
            card_number = random.randint(999999999, 10000000000)

        if not email:
            email = Utilities.generate_email()

        RentSummaryPage.enter_name(name)
        RentSummaryPage.enter_last_name(last_name)
        RentSummaryPage.enter_card_number(card_number)
        RentSummaryPage.enter_email(email)

    @classmethod
    def rent_car(cls):
        RentSummaryPage.rent_car()

    @classmethod
    def verify_successful_rent(cls):
        pass  # TODO: Implement success message verification once it is implemented in the app
