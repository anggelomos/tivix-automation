from src.pages.base_page import BasePage
from src.pages.locators.rent_summary_locators import RentSummaryLocators


class RentSummaryPage(BasePage):

    @classmethod
    def enter_name(cls, name):
        RentSummaryLocators.name_input().send_keys(name)

    @classmethod
    def enter_last_name(cls, last_name):
        RentSummaryLocators.last_name_input().send_keys(last_name)

    @classmethod
    def enter_card_number(cls, card_number):
        RentSummaryLocators.card_number_input().send_keys(card_number)

    @classmethod
    def enter_email(cls, email):
        RentSummaryLocators.email_input().send_keys(email)

    @classmethod
    def rent_car(cls):
        RentSummaryLocators.rent_button().click()
