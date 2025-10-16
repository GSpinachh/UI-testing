import time
from selenium.webdriver.common.by import By
from .base_page import BasePage

class LoginPage(BasePage):
    URL = "https://www.way2automation.com/angularjs-protractor/registeration/#/login"
    
    USERNAME_FIELD = (By.XPATH, "//input[1]")
    PASSWORD_FIELD = (By.XPATH, "//input[2]")
    USERNAME2_FIELD = (By.XPATH, "//input[3]")
    LOGIN_BUTTON = (By.XPATH, "//button[contains(., 'Login')]")
    SUCCESS_MESSAGE = (By.XPATH, "//*[contains(., 'logged in!!')]")
    ERROR_MESSAGE = (By.XPATH, "//*[contains(., 'incorrect')]")
    
    def open(self):
        self.driver.get(self.URL)
        time.sleep(3)
    
    def login(self, username, password, username2):
        inputs = self.driver.find_elements(By.TAG_NAME, "input")
        if len(inputs) >= 3:
            inputs[0].clear(); inputs[0].send_keys(username)
            inputs[1].clear(); inputs[1].send_keys(password)
            inputs[2].clear(); inputs[2].send_keys(username2)
            time.sleep(1)
        
        button = self.find_element(*self.LOGIN_BUTTON)
        if button and button.is_enabled():
            button.click()
            return True
        return False
    
    def login_with_valid_credentials(self):
        return self.login("angular", "password", "angular")
    
    def login_with_invalid_credentials(self):
        return self.login("incorrect", "incorrect", "incorrect")
    
    def is_login_button_disabled(self):
        button = self.find_element(*self.LOGIN_BUTTON)
        return button is not None and not button.is_enabled()
    
    def is_success_message_displayed(self):
        element = self.find_element(*self.SUCCESS_MESSAGE, timeout=5)
        return element is not None
    
    def is_error_message_displayed(self):
        element = self.find_element(*self.ERROR_MESSAGE, timeout=5)
        return element is not None
    
    def logout(self):
        logout_btn = self.find_element(By.XPATH, "//button[contains(., 'Logout')]")
        if logout_btn:
            logout_btn.click()
            time.sleep(2)
            return True
        return False