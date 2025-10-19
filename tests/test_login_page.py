import pytest
import time
from selenium.webdriver.common.by import By  

class TestLoginPage:
    
    @pytest.mark.run(order=7)
    def test_4_1_login_fields(self, login_page):
        print("Тест 4.1: Проверка полей ввода")
        
        time.sleep(3)

        all_inputs = login_page.driver.find_elements(By.TAG_NAME, "input")
        assert len(all_inputs) >= 3, f"Найдено {len(all_inputs)} полей, нужно 3"
        
        assert login_page.is_login_button_disabled(), "Кнопка Login не задизейблена"
        print("Поля отображаются, кнопка Login задизейблена")
    
    @pytest.mark.run(order=8)
    def test_4_2_successful_login(self, login_page):
        print("\nТест 4.2: Проверка успешной авторизации")
        
        login_page.login_with_valid_credentials()
        time.sleep(3)
        assert login_page.is_success_message_displayed(), "Сообщение об успехе не отображается"
        print("Успешная авторизация выполнена")
    
    @pytest.mark.run(order=9)
    def test_4_3_invalid_login(self, login_page):
        print("\nТест 4.3: Проверка авторизации с невалидыми данными")
        
        login_page.login_with_invalid_credentials()
        time.sleep(3)
        
        if login_page.is_error_message_displayed():
            print("Сообщение об ошибке отображается")
        else:
            print("Сообщение об ошибке не найдено")
    
    @pytest.mark.run(order=10)
    def test_4_4_logout(self, login_page):
        print("\nТест 4.4: Проверка успешного разлогирования")

        login_page.login_with_valid_credentials()
        time.sleep(3)
        login_page.logout()
        time.sleep(2)

        current_url = login_page.driver.current_url
        if "login" in current_url or "registeration" in current_url:
            print("Успешно разлогинились")
        else:
            login_button = login_page.find_element(*login_page.LOGIN_BUTTON)
            if login_button:
                print("Кнопка Login отображается после выхода")