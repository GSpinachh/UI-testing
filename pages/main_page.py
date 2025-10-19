from selenium.webdriver.common.by import By
from .base_page import BasePage

class MainPage(BasePage):
    URL = "https://www.way2automation.com/"
    
    HEADER = (By.TAG_NAME, "header")
    NAVIGATION = (By.TAG_NAME, "nav")
    REGISTER_BUTTON = (By.XPATH, "//a[contains(., 'Register')]")
    COURSES_SECTION = (By.XPATH, "//*[contains(text(), 'Best Selenium')]")
    FOOTER = (By.ID, "colophon")
    
    def open(self):
        self.driver.get(self.URL)
    
    def is_header_displayed(self):
        return self.find_element(*self.HEADER) is not None
    
    def is_navigation_displayed(self):
        return self.find_element(*self.NAVIGATION) is not None
    
    def is_register_button_displayed(self):
        return self.find_element(*self.REGISTER_BUTTON) is not None
    
    def is_courses_section_displayed(self):
        return self.find_element(*self.COURSES_SECTION) is not None
    
    def is_footer_displayed(self):
        footer = self.find_element(*self.FOOTER)
        return footer is not None and footer.is_displayed()
    
    def get_contact_info(self):
        phones = self.find_elements(By.XPATH, "//a[contains(@href, 'tel:')]")
        emails = self.find_elements(By.XPATH, "//a[contains(@href, 'mailto:')]")
        social_links = self.find_elements(By.XPATH, "//a[contains(@href, 'facebook') or contains(@href, 'twitter')]")
        
        return {
            'phones': phones,
            'emails': emails,
            'social_links': social_links
        }
    
    def navigate_to_lifetime_membership(self):
        self.driver.get("https://www.way2automation.com/lifetime-membership-club/")
        return "lifetime-membership-club" in self.driver.current_url