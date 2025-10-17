from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)
    
    def find_element(self, by, value, timeout=10):
        try:
            return WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
        except TimeoutException:
            return None
    
    def find_elements(self, by, value, timeout=10):
        try:
            WebDriverWait(self.driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return self.driver.find_elements(by, value)
        except TimeoutException:
            return []
    
    def click_element(self, by, value):
        element = self.find_element(by, value)
        if element:
            element.click()
            return True
        return False
    
    def send_keys(self, by, value, text):
        element = self.find_element(by, value)
        if element:
            element.clear()
            element.send_keys(text)
            return True
        return False
    
    def select_dropdown_by_visible_text(self, by, value, text):
        from selenium.webdriver.support.ui import Select
        element = self.find_element(by, value)
        if element:
            select = Select(element)
            select.select_by_visible_text(text)
            return True
        return False
    
    def wait_for_alert(self, timeout=5):
        try:
            WebDriverWait(self.driver, timeout).until(EC.alert_is_present())
            return self.driver.switch_to.alert
        except TimeoutException:
            return None
    
    def accept_alert(self):
        alert = self.wait_for_alert()
        if alert:
            alert.accept()
            return True
        return False
    
    def get_alert_text(self):
        alert = self.wait_for_alert()
        if alert:
            return alert.text
        return None
    
    def is_element_displayed(self, by, value):
        element = self.find_element(by, value)
        return element is not None and element.is_displayed()
    
    def get_element_text(self, by, value):
        element = self.find_element(by, value)
        return element.text if element else ""