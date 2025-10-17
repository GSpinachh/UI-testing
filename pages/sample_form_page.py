import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select
from .base_page import BasePage

class SampleFormPage(BasePage):
    
    URL = "https://www.way2automation.com/angularjs-protractor/banking/#/login"
    SAMPLE_FORM_LINK = (By.XPATH, "//a[contains(text(), 'Sample Form')]")
    
    def open_sample_form(self):
        self.driver.get(self.URL)
        time.sleep(2)
        self.click_element(*self.SAMPLE_FORM_LINK)
        time.sleep(3)
    
    def get_longest_hobby_word(self):
        hobbies = ["Cricket", "Movies", "Hockey"]
        return max(hobbies, key=len)
    
    def fill_registration_form(self, first_name, last_name):
        longest_word = self.get_longest_hobby_word()
        about_text = f"Самое длинное слово из предложенных хобби - {longest_word}"
        
        print(f"Заполнение формы для {first_name} {last_name}")
        print(f"Самое длинное слово хобби: {longest_word}")
        print(f"Текст About Yourself: {about_text}")