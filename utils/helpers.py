import time
from datetime import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException

class Helpers:
    
    @staticmethod
    def take_screenshot(driver, test_name):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"screenshots/{test_name}_{timestamp}.png"
        driver.save_screenshot(filename)
        return filename
    
    @staticmethod
    def wait_for_page_load(driver, timeout=10):
        try:
            WebDriverWait(driver, timeout).until(
                lambda d: d.execute_script("return document.readyState") == "complete"
            )
            return True
        except TimeoutException:
            return False
    
    @staticmethod
    def wait_for_angular(driver, timeout=10):
        try:
            WebDriverWait(driver, timeout).until(
                lambda d: d.execute_script("return window.angular !== undefined")
            )
            time.sleep(2) 
            return True
        except TimeoutException:
            return False
    
    @staticmethod
    def is_element_present(driver, by, value, timeout=5):
        try:
            WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((by, value))
            )
            return True
        except TimeoutException:
            return False
    
    @staticmethod
    def is_element_visible(driver, by, value, timeout=5):
        try:
            WebDriverWait(driver, timeout).until(
                EC.visibility_of_element_located((by, value))
            )
            return True
        except TimeoutException:
            return False
    
    @staticmethod
    def wait_for_element_clickable(driver, by, value, timeout=10):
        try:
            WebDriverWait(driver, timeout).until(
                EC.element_to_be_clickable((by, value))
            )
            return True
        except TimeoutException:
            return False
    
    @staticmethod
    def scroll_to_element(driver, element):
        driver.execute_script("arguments[0].scrollIntoView({behavior: 'smooth', block: 'center'});", element)

helpers = Helpers()