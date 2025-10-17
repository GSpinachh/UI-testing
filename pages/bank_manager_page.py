import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from .base_page import BasePage

class BankManagerPage(BasePage):
    URL = "https://www.way2automation.com/angularjs-protractor/banking/#/login"
    
    BANK_MANAGER_LOGIN = (By.XPATH, "//button[contains(text(), 'Bank Manager Login')]")
    
    ADD_CUSTOMER_BUTTON = (By.XPATH, "//button[contains(text(), 'Add Customer')]")
    OPEN_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(text(), 'Open Account')]")
    CUSTOMERS_BUTTON = (By.XPATH, "//button[contains(text(), 'Customers')]")
    
    CUSTOMER_FIRST_NAME = (By.XPATH, "//input[@ng-model='fName']")
    CUSTOMER_LAST_NAME = (By.XPATH, "//input[@ng-model='lName']")
    CUSTOMER_POST_CODE = (By.XPATH, "//input[@ng-model='postCd']")
    SUBMIT_CUSTOMER_BUTTON = (By.XPATH, "//button[@type='submit']")
    
    CUSTOMER_SELECT = (By.ID, "userSelect")
    CURRENCY_SELECT = (By.ID, "currency")
    PROCESS_BUTTON = (By.XPATH, "//button[text()='Process']")
    
    SEARCH_CUSTOMER = (By.XPATH, "//input[@placeholder='Search Customer']")
    DELETE_CUSTOMER_BUTTON = (By.XPATH, "//button[text()='Delete']")
    CUSTOMER_ROWS = (By.XPATH, "//table//tr[position()>1]")
    
    def login_as_bank_manager(self):
        self.driver.get(self.URL)
        time.sleep(2)
        self.click_element(*self.BANK_MANAGER_LOGIN)
        time.sleep(2)
    
    def add_customer(self, first_name, last_name, post_code):
        self.click_element(*self.ADD_CUSTOMER_BUTTON)
        time.sleep(2)
        
        self.send_keys(*self.CUSTOMER_FIRST_NAME, first_name)
        self.send_keys(*self.CUSTOMER_LAST_NAME, last_name)
        self.send_keys(*self.CUSTOMER_POST_CODE, post_code)
        
        self.click_element(*self.SUBMIT_CUSTOMER_BUTTON)
        time.sleep(2)
        
        alert_text = self.get_alert_text()
        if alert_text:
            self.accept_alert()
            return alert_text
        return "Customer added successfully"
    
    def open_account(self, customer_name, currency="Dollar"):
        self.click_element(*self.OPEN_ACCOUNT_BUTTON)
        time.sleep(2)
        
        self.select_dropdown_by_visible_text(*self.CUSTOMER_SELECT, customer_name)
        
        self.select_dropdown_by_visible_text(*self.CURRENCY_SELECT, currency)
        
        self.click_element(*self.PROCESS_BUTTON)
        time.sleep(2)
        
        alert_text = self.get_alert_text()
        if alert_text:
            self.accept_alert()
            return alert_text
        return "Account created successfully"
    
    def delete_customer(self, first_name):
        self.click_element(*self.CUSTOMERS_BUTTON)
        time.sleep(2)
        
        self.send_keys(*self.SEARCH_CUSTOMER, first_name)
        time.sleep(1)
        
        self.click_element(*self.DELETE_CUSTOMER_BUTTON)
        time.sleep(2)
        
        search_field = self.find_element(*self.SEARCH_CUSTOMER)
        if search_field:
            search_field.clear()
        time.sleep(1)
    
    def is_customer_present(self, first_name):
        self.click_element(*self.CUSTOMERS_BUTTON)
        time.sleep(1)
        
        self.send_keys(*self.SEARCH_CUSTOMER, first_name)
        time.sleep(1)
        
        rows = self.find_elements(*self.CUSTOMER_ROWS)
        
        search_field = self.find_element(*self.SEARCH_CUSTOMER)
        if search_field:
            search_field.clear()
            
        return len(rows) > 0