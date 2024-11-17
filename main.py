
from module import check_stock, calculate_order_price
from module import register_user
from module import send_notification
from module import process_order
from module import check_user_age
from module import validate_address
from module import apply_discount, add_product_to_cart, process_payment

def main():
    stock = {"Фен": 10, "Лак": 5}
    cart = {}

    try:
        # Проверка наличия товара
        check_stock("Фен", 2, stock)
        
        # Расчёт стоимости заказа
        print(calculate_order_price(100, 2, 10))
        
        # Регистрация пользователя
        register_user("Виктория", "Виктория@yndex.ru")
        
        # Отправка уведомления
        send_notification("Виктория@yndex.ru", "Ваш заказ подтверждён")

        send_notification("Виктория@GMAIL.ru", "Ваш заказ подтверждён")
        
        # Обработка заказа
        process_order({"items": [{"price": 100, "quantity": 2}], "address": "Прянишкаво 2А"})
        
        # Проверка возраста
        check_user_age(20)
        
        # Проверка адреса доставки
        validate_address("Пря")
        validate_address("Прянишкаво 2А")
        # Применение скидки
        print(apply_discount(200, "SALE10"))
        
        # Добавление товара в корзину
        add_product_to_cart(cart, "Лак", 3, stock)
        
        # Обработка оплаты
        process_payment(150)
    except Exception as e:
        print(f"Ошибка: {e}")

if __name__ == "__main__":
    main()
