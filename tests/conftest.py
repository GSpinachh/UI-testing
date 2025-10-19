import pytest
from selenium import webdriver

@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture
def main_page(driver):
    from pages.main_page import MainPage
    page = MainPage(driver)
    page.open()
    return page

@pytest.fixture
def login_page(driver):
    from pages.login_page import LoginPage
    page = LoginPage(driver)
    page.open()
    return page