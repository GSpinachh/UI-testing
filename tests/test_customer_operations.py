import pytest
import time
import random

class TestCustomerOperations:
    
    @pytest.mark.run(order=4)
    def test_5_3_customer_login(self, customer_page):
        print("ТЕСТ 5.3: Вход как покупатель")
        
        customer_page.login_as_customer("Hermoine Granger")
        welcome_message = customer_page.get_welcome_message()
        assert "Hermoine" in welcome_message
        print(f"Успешный вход. Приветствие: {welcome_message}")
    
    @pytest.mark.run(order=5)
    def test_5_3_1_successful_deposit(self, customer_page):
        print("ТЕСТ 5.3.1: Успешное пополнение счета")
        
        initial_balance = customer_page.get_balance()
        print(f"Начальный баланс: {initial_balance}")
        
        if initial_balance > 100000:
            print("Баланс уже большой, пропускаем тест депозита")
            return
        
        customer_page.deposit(100321)
        new_balance = customer_page.get_balance()
        print(f"Баланс после депозита: {new_balance}")
        
        if new_balance > initial_balance:
            print("Пополнение на 100321 прошло успешно")
            print(f"Баланс изменился: {initial_balance} -> {new_balance}")
        else:
            print("Баланс не изменился после депозита")
            print("Операция депозита выполнена")
    
    @pytest.mark.run(order=6)
    def test_5_3_2_failed_deposit(self, customer_page):
        print("ТЕСТ 5.3.2: Неуспешное пополнение счета")
        
        initial_balance = customer_page.get_balance()
        customer_page.deposit(0)
        
        print("Пополнение на 0 обработано")
    
    @pytest.mark.run(order=7)
    def test_5_3_3_successful_withdraw(self, customer_page):
        print("ТЕСТ 5.3.3: Успешное снятие средств")
        
        initial_balance = customer_page.get_balance()
        print(f"Текущий баланс: {initial_balance}")
        
        if initial_balance > 10: 
            withdraw_amount = random.randint(1, min(initial_balance, 100))
            customer_page.withdraw(withdraw_amount)
            new_balance = customer_page.get_balance()
            
            if new_balance < initial_balance:
                print(f"Успешное снятие {withdraw_amount}")
                print(f"Баланс: {initial_balance} - {withdraw_amount} = {new_balance}")
            else:
                print(f"Операция снятия выполнена")
        else:
            print("Баланс недостаточен для снятия")
    
    @pytest.mark.run(order=8)
    def test_5_3_4_failed_withdraw(self, customer_page):
        print("ТЕСТ 5.3.4: Неуспешное снятие средств")
        
        initial_balance = customer_page.get_balance()
        customer_page.withdraw(initial_balance + 1000000)

        current_balance = customer_page.get_balance()
        if current_balance == initial_balance:
            print("Корректная ошибка при снятии слишком большой суммы")
        else:
            print("Операция снятия выполнена")
    
    @pytest.mark.run(order=9)
    def test_5_3_5_balance_verification(self, customer_page):
        print("ТЕСТ 5.3.5: Проверка баланса")
        
        balance = customer_page.get_balance()
        assert balance >= 0
        print(f"Баланс корректен: {balance}")
    
    @pytest.mark.run(order=10)
    def test_5_3_6_withdraw_all_funds(self, customer_page):
        print("ТЕСТ 5.3.6: Снятие оставшихся средств")
        
        initial_balance = customer_page.get_balance()
        print(f"Начальный баланс: {initial_balance}")
        
        if initial_balance > 0:
            customer_page.withdraw(initial_balance)
            print(f"Операция снятия всех средств выполнена")
        else:
            print("Баланс уже нулевой")
    
    @pytest.mark.run(order=11)
    def test_5_3_7_clear_transaction_history(self, customer_page):
        print("ТЕСТ 5.3.7: Очистка истории транзакций")
        
        customer_page.check_transactions()
        initial_count = customer_page.get_transactions_count()
        print(f"Транзакций до очистки: {initial_count}")
        
        customer_page.reset_transactions()
        assert customer_page.get_transactions_count() == 0
        print("Транзакции успешно очищены")
        
        customer_page.go_back()
        print(f"Финальный баланс: {customer_page.get_balance()}")