Django Test Payment API

Это проект на Django для тестирования платежного API с использованием Stripe. Проект включает базовые функции для управления товарами, заказами и интеграции Stripe для обработки платежей.

Структура проекта

Django_test_payment_api/
├── __init__.py
├── admin.py
├── apps.py
├── asgi.py
├── models.py
├── settings.py
├── tests.py
├── urls.py
├── views.py
├── wsgi.py
testapp/
├── __init__.py
├── admin.py
├── apps.py
├── migrations/
├── models.py
├── templates/
│   ├── cart_detail.html
│   ├── index.html
│   ├── item_detail.html
│   ├── order_detail.html
├── tests.py
├── urls.py
├── views.py
manage.py
requirements.txt
Dockerfile

Требования

- Python 3.9
- Django 4.2.19
- Stripe 11.0.0

Установка

1. Клонируйте репозиторий:

git clone https://github.com/yourusername/Django-test-payment-api.git
cd Django-test-payment-api

2. Создайте и активируйте виртуальное окружение:

python -m venv venv
source venv/bin/activate  # В Windows используйте `venv\Scripts\activate`

3. Установите зависимости:

pip install -r requirements.txt

4. Примените миграции:

python manage.py migrate

5. Создайте суперпользователя:

python manage.py createsuperuser

6. Запустите сервер разработки:

python manage.py runserver

Docker

Чтобы запустить проект с использованием Docker, выполните следующие шаги:

1. Соберите Docker-образ:

docker build -t django-test-payment-api .

2. Запустите Docker-контейнер:

docker run -p 8000:8000 django-test-payment-api

Использование

- Доступ к админ-панели по адресу `http://localhost:8000/admin/` с использованием учетных данных суперпользователя.
- Добавляйте товары в базу данных через админ-панель.
- Перейдите на главную страницу по адресу `http://localhost:8000/`, чтобы увидеть список товаров.
- Добавляйте товары в корзину и переходите к оплате с использованием Stripe.

Подробности проекта

Модели

- `Item`: Представляет товар с именем, описанием и ценой.
- `Order`: Представляет заказ с списком товаров, датой создания и статусом (активен или оплачен).
- `OrderItem`: Представляет товар в заказе с количеством.

Представления (Views)

- `main_page`: Отображает список товаров.
- `buy_item`: Создает сессию Stripe для оплаты одного товара.
- `item_detail`: Отображает детали товара.
- `order_detail`: Отображает детали заказа.
- `buy_order`: Создает сессию Stripe для оплаты всего заказа.
- `add_to_cart`: Добавляет товар в корзину.
- `cart_detail`: Отображает детали корзины.
- `update_cart_item`: Обновляет количество товара в корзине.
- `remove_from_cart`: Удаляет товар из корзины.

Шаблоны (Templates)

- `index.html`: Шаблон главной страницы.
- `item_detail.html`: Шаблон страницы деталей товара.
- `cart_detail.html`: Шаблон страницы деталей корзины.
- `order_detail.html`: Шаблон страницы деталей заказа.

Лицензия

Этот проект лицензирован по лицензии MIT. См. файл LICENSE для получения подробной информации.