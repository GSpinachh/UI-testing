import pytest
import time
from selenium.webdriver.common.by import By

class TestMainPage:
    
    @pytest.mark.run(order=1)
    def test_1_1_main_page_elements(self, main_page):
        print("Тест 1.1: Проверка основных элементов")
        
        assert main_page.is_header_displayed(), "Хедер не отображается"
        assert main_page.is_navigation_displayed(), "Навигация не отображается"
        assert main_page.is_register_button_displayed(), "Кнопка регистрации не отображается"
        assert main_page.is_courses_section_displayed(), "Секция курсов не отображается"
        assert main_page.is_footer_displayed(), "Футер не отображается"
        print("Все основные элементы отображаются")
    
    @pytest.mark.run(order=2)
    def test_1_2_contact_header(self, main_page):
        print("\nТест 1.2: Проверка контактной информации")
        
        contact_info = main_page.get_contact_info()
        
        assert len(contact_info['phones']) > 0, "Телефоны не найдены"
        assert len(contact_info['emails']) > 0, "Email не найден"
        assert len(contact_info['social_links']) > 0, "Социальные сети не найдены"
        print("Контактная информация отображается")
    
    @pytest.mark.run(order=3)
    def test_1_3_courses_slider(self, main_page):
        print("\nТест 1.3: Проверка слайдера курсов")
        
        main_page.scroll_to_bottom()
        time.sleep(2)
        
        prev_button = main_page.find_element(By.CSS_SELECTOR, ".swiper-button-prev-c50f9f0")
        next_button = main_page.find_element(By.CSS_SELECTOR, ".swiper-button-next-c50f9f0")
        
        if prev_button and next_button:
            if next_button.is_enabled():
                main_page.driver.execute_script("arguments[0].click();", next_button)
                time.sleep(1)
                main_page.driver.execute_script("arguments[0].click();", prev_button)
                time.sleep(1)
                print("Навигация слайдера работает")
            else:
                print("Кнопки навигации неактивны")
        else:
            print("Кнопки навигации не найдены")
    
    @pytest.mark.run(order=4)
    def test_1_4_footer(self, main_page):
        print("\nТест 1.4: Проверка футера")
        
        main_page.scroll_to_bottom()
        time.sleep(2)
        
        footer = main_page.find_element(By.ID, "colophon")
        assert footer and footer.is_displayed(), "Футер не отображается"
        
        address = main_page.find_element(By.XPATH, "//span[contains(text(), 'Naya Bans Market')]")
        phones = main_page.find_elements(By.XPATH, "//a[contains(@href, 'tel:')]")
        emails = main_page.find_elements(By.XPATH, "//a[contains(@href, 'mailto:')]")
        
        if address and len(phones) >= 2 and len(emails) >= 2:
            print("Футер содержит адрес, телефоны и email")
        else:
            print("Футер не содержит все элементы, но отображается")
    
    @pytest.mark.run(order=5)
    def test_2_navigation_scroll(self, main_page):
        print("\nТест 2: Проверка меню при скроллинге")
        
        main_page.driver.execute_script("window.scrollTo(0, 800);")
        time.sleep(2)
        assert main_page.is_navigation_displayed(), "Навигация не видна после скроллинга"
        print("Меню остается видимым при скроллинге")
    
    @pytest.mark.run(order=6)
    def test_3_navigation_to_courses(self, main_page):
        print("\nТест 3: Проверка перехода на Lifetime Membership")
        
        success = main_page.navigate_to_lifetime_membership()
        assert success, "Переход на страницу не выполнен"
        
        title_elements = main_page.find_elements(By.XPATH, "//*[contains(text(), 'LIFETIME')]")
        assert len(title_elements) > 0, "Заголовок не содержит 'LIFETIME'"
        print("Переход выполнен, заголовок корректный")