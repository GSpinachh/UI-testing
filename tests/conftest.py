import pytest
from selenium import webdriver
import os

@pytest.fixture
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    options.add_argument('--disable-extensions')
    options.add_argument('--disable-gpu')
    options.add_argument('--no-sandbox')
    
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(10)
    yield driver
    driver.quit()

@pytest.fixture
def sample_form_page(driver):
    from pages.sample_form_page import SampleFormPage
    page = SampleFormPage(driver)
    return page

@pytest.fixture
def bank_manager_page(driver):
    from pages.bank_manager_page import BankManagerPage
    page = BankManagerPage(driver)
    return page

@pytest.fixture  
def customer_page(driver):
    from pages.customer_page import CustomerPage
    page = CustomerPage(driver)
    return page

@pytest.fixture
def customer_data():
    import random
    return {
        'first_name': f'TestUser{random.randint(1000, 9999)}',
        'last_name': 'AutoTest',
        'post_code': f'PC{random.randint(10000, 99999)}'
    }