import pytest
from pytest_bdd import scenario, given, when, then


@pytest.fixture(scope="module", autouse=True)
def setup():
    BasePage.start_browser()
    yield


@pytest.fixture(scope="module", autouse=True)
def teardown():
    yield
    BasePage.close_browser()


@scenario('automation_tivix_.feature', 'Rent a car successfully')
def test_user_with_permissions_tries_to_access_a_resource():
    pass  # pytest-bdd function


@given("that I am on the main rent page")
def go_to_main_page():
    CarRentController.go_to_main_page()


@when("I do the process to rent a car")
def rent_a_car_successfully():
    CarRentController.search_car()
    CarRentController.verify_rent_information()
    CarRentController.enter_personal_data()


@then("I rent a car successfully")
def verify_car_rented_successfully():
    CarRentController.verify_successfull_rent()