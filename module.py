
#1 Две функции без обработки исключений

#Проверка наличия товара на складе
def check_stock(product_id, quantity, stock):
    """Проверяет, доступно ли нужное количество товара на складе."""
    if product_id not in stock:
        raise KeyError(f"Товар с ID {product_id} отсутствует")
    if stock[product_id] < quantity:
        raise ValueError("Недостаточное количество товара на складе")
    return True

#Расчет стоимости заказа с учётом скидки
def calculate_order_price(price, quantity, discount):
    """Расчет стоимости с учётом скидки."""
    if discount < 0 or discount > 100:
        raise ValueError("Некорректное значение скидки")
    if quantity < 1:
        raise ValueError("Количество должно быть больше нуля")
    total_price = price * quantity * (1 - discount / 100)
    return total_price


#2  Функция с одним обработчиком исключений Регистрирует пользователя в системе

def register_user(username, email):
     
    try:
        if "@" not in email:
            raise ValueError("Некорректный email")
        if len(username) < 3:
            raise ValueError("Имя пользователя слишком короткое")
        print(f"Пользователь {username} успешно зарегистрирован")
        return True
    except Exception as e:
        print(f"Ошибка при регистрации: {e}")
        return False
#3 Функция с обработчиком и finally

# Отправляет email-уведомление пользователю

def send_notification(user_email, message):
    try:
        if not user_email.endswith("@yndex.ru"):
            raise ValueError("Некорректный email домен")
        print(f"Отправка сообщения: {message} на {user_email}")
    except Exception as e:
        print(f"Ошибка отправки уведомления: {e}")
    finally:
        print("Уведомление обработано.")

#4 Функции с несколькими обработчиками исключений

# Обрабатывает заказ и рассчитывает доставку.

def process_order(order):
    try:
        # Проверка наличия товаров
        if not order.get("items"):
            raise KeyError("Пустой заказ")
        
        # Проверка, что сумма заказа не отрицательна
        total = sum(item['price'] * item['quantity'] for item in order["items"])
        if total < 0:
            raise ValueError("Сумма заказа не может быть отрицательной")
        
        # Проверка адреса доставки
        if "address" not in order or not order["address"]:
            raise AttributeError("Адрес доставки не указан")
        
        print(f"Заказ на сумму {total} обработан")
    except KeyError as e:
        print(f"Ошибка в заказе: {e}")
    except ValueError as e:
        print(f"Ошибка расчета стоимости: {e}")
    except AttributeError as e:
        print(f"Ошибка доставки: {e}")
    finally:
        print("Обработка заказа завершена.")

#5 Генерация исключений внутри функции
# Проверяет возраст для оформления заказа.

def check_user_age(age):
    try:
        if age < 0:
            raise ValueError("Возраст не может быть отрицательным")
        if age < 18:
            raise PermissionError("Пользователь должен быть старше 18 лет для оформления заказа")
        print("Возраст пользователя подтверждён")
    except ValueError as e:
        print(f"Ошибка: {e}")
    except PermissionError as e:
        print(f"Ошибка доступа: {e}")
    finally:
        print("Проверка возраста завершена")

#6 Пользовательские исключения

class ProductNotFoundError(Exception):
    pass

class PaymentError(Exception):
    pass

class AddressError(Exception):
    pass

#7 Использование пользовательских исключений
# Проверка корректности адреса доставки.

def validate_address(address):
    try:
        if not address or len(address) < 10:
            raise AddressError("Адрес слишком короткий или отсутствует")
        print("Адрес подтверждён")
    except AddressError as e:
        print(f"Ошибка адреса: {e}")
    finally:
        print("Проверка адреса завершена")

#8Дополнительные функции для демонстрации
 

def apply_discount(price, discount_code):
    # Применяет скидку по коду
    valid_codes = {"SALE10": 10, "DISCOUNT20": 20}
    if discount_code not in valid_codes:
        raise KeyError("Некорректный код скидки")
    return price * (1 - valid_codes[discount_code] / 100)

def add_product_to_cart(cart, product_id, quantity, stock):
    """Добавляет товар в корзину."""
    if product_id not in stock:
        raise KeyError("Товар не найден")
    if quantity > stock[product_id]:
        raise ValueError("Недостаточное количество товара")
    cart[product_id] = quantity
    return cart

def process_payment(amount):
    """Обрабатывает оплату."""
    if amount <= 0:
        raise ValueError("Сумма должна быть положительной")
    print(f"Платёж на сумму {amount} обработан")
