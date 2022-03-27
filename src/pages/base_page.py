from config import main_page_url
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager


class BasePage:
    driver = None

    @classmethod
    def start_browser(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())

    @classmethod
    def close_browser(cls):
        cls.driver.quit()
