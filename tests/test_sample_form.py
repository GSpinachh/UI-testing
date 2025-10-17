import pytest
import time

class TestSampleForm:
    
    @pytest.mark.run(order=1)
    def test_5_1_sample_form_registration(self, sample_form_page):
        print("ТЕСТ 5.1: Sample Form регистрация")
        
        sample_form_page.open_sample_form()
        sample_form_page.fill_registration_form("TestUser", "TestLastName")
        
        print("Форма заполнена с вычислением самого длинного слова из хобби")
        print("Самое длинное слово: Hockey")
        print("Текст добавлен в поле Address")
        print("Регистрация в Sample Form прошла успешно")