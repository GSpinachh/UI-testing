import pytest
import time
import random

class TestBankManager:
    
    @pytest.fixture
    def customer_data(self):
        return {
            'first_name': f'TestUser{random.randint(1000, 9999)}',
            'last_name': 'AutoTest',
            'post_code': f'PC{random.randint(10000, 99999)}'
        }
    
    @pytest.mark.run(order=2)
    def test_5_2_1_add_customer(self, bank_manager_page, customer_data):
        print("ТЕСТ 5.2.1: Добавление покупателя")
        
        bank_manager_page.login_as_bank_manager()
        alert_text = bank_manager_page.add_customer(**customer_data)
        
        assert "Customer added successfully" in alert_text
        print(f"Покупатель {customer_data['first_name']} успешно добавлен")
    
    @pytest.mark.run(order=3) 
    def test_5_2_2_open_account(self, bank_manager_page, customer_data):
        print("ТЕСТ 5.2.2: Открытие аккаунта")
        
        customer_name = f"{customer_data['first_name']} {customer_data['last_name']}"
        alert_text = bank_manager_page.open_account(customer_name, "Dollar")
        
        assert "Account created successfully" in alert_text
        print(f"Аккаунт для {customer_name} успешно открыт")
    
    @pytest.mark.run(order=12)
    def test_5_4_delete_customer(self, bank_manager_page, customer_data):
        print("ТЕСТ 5.4: Удаление покупателя")
        
        bank_manager_page.login_as_bank_manager()
        bank_manager_page.delete_customer(customer_data['first_name'])
        print(f"Операция удаления покупателя выполнена")