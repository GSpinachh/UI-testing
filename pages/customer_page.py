import time
import random
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from .base_page import BasePage

class CustomerPage(BasePage):
    
    URL = "https://www.way2automation.com/angularjs-protractor/banking/#/login"
    
    CUSTOMER_LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Customer Login')]")
    CUSTOMER_SELECT = (By.ID, "userSelect")
    LOGIN_BUTTON = (By.XPATH, "//button[text()='Login']")
    WELCOME_MESSAGE = (By.XPATH, "//span[@class='fontBig ng-binding']")
    BALANCE = (By.XPATH, "//div[@ng-hide='noAccount']/strong[2]")
    ACCOUNT_SELECT = (By.ID, "accountSelect")  
    DEPOSIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Deposit')]")
    WITHDRAWL_BUTTON = (By.XPATH, "//button[contains(text(), 'Withdrawl')]")
    TRANSACTIONS_BUTTON = (By.XPATH, "//button[contains(text(), 'Transactions')]")
    DEPOSIT_AMOUNT = (By.XPATH, "//input[@type='number']")
    DEPOSIT_SUBMIT = (By.XPATH, "//button[@type='submit']")
    WITHDRAWL_AMOUNT = (By.XPATH, "//input[@type='number']")
    WITHDRAWL_SUBMIT = (By.XPATH, "//button[@type='submit']")
    MESSAGE_ELEMENT = (By.XPATH, "//span[@class='error ng-binding']")
    RESET_BUTTON = (By.XPATH, "//button[contains(text(), 'Reset')]")
    BACK_BUTTON = (By.XPATH, "//button[contains(text(), 'Back')]")
    TRANSACTION_ROWS = (By.XPATH, "//table//tr[position()>1]")
    
    def login_as_customer(self, customer_name):
        self.driver.get(self.URL)
        time.sleep(2)
        self.click_element(*self.CUSTOMER_LOGIN_BUTTON)
        time.sleep(2)
        
        customer_select = self.find_element(*self.CUSTOMER_SELECT)
        if customer_select:
            select = Select(customer_select)
            select.select_by_index(1) 
            self.click_element(*self.LOGIN_BUTTON)
            time.sleep(2)

            account_select = self.find_element(*self.ACCOUNT_SELECT)
            if account_select:
                select = Select(account_select)
                if len(select.options) > 1:
                    select.select_by_index(1)  
                    time.sleep(1)
            return True
        return False
    
    def get_welcome_message(self):
        return self.get_element_text(*self.WELCOME_MESSAGE)
    
    def get_balance(self):
        balance_text = self.get_element_text(*self.BALANCE)
        try:
            return int(balance_text)
        except ValueError:
            return 0
    
    def deposit(self, amount):
        self.click_element(*self.DEPOSIT_BUTTON)
        time.sleep(1)
        self.send_keys(*self.DEPOSIT_AMOUNT, str(amount))
        self.click_element(*self.DEPOSIT_SUBMIT)
        time.sleep(2)
        
    def withdraw(self, amount):
        self.click_element(*self.WITHDRAWL_BUTTON)
        time.sleep(1)
        self.send_keys(*self.WITHDRAWL_AMOUNT, str(amount))
        self.click_element(*self.WITHDRAWL_SUBMIT)
        time.sleep(2)
    
    def check_transactions(self):
        self.click_element(*self.TRANSACTIONS_BUTTON)
        time.sleep(1)
    
    def get_transactions_count(self):
        self.check_transactions()
        return len(self.find_elements(*self.TRANSACTION_ROWS))
    
    def reset_transactions(self):
        self.check_transactions()
        self.click_element(*self.RESET_BUTTON)
        time.sleep(1)
    
    def go_back(self):
        self.click_element(*self.BACK_BUTTON)
        time.sleep(1)