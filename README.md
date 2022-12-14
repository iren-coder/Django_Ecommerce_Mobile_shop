Данный проект представляет собой магазин-приложение мобильных телефонов. 

Django, Sqlite3, Bootstrap, Django AllAuth, Django Countries

Проект разработан на основе фреймворка Django, используемая БД SQLite, вёрстка на основе Bootstrap 4.
Приложение является полноценным интерент-магазином (привязка систем оплат в процессе).

![Вход на сайт](/screenshots/main.png)

![Вход на сайт](/screenshots/product.png)

Приложение позволяет пользователю:
- регистрироваться и авторизовываться пользователям (django-allauth)
- искать товар по марке или полному наименованию
- открывать карточку каждого продукта с подробным описанием
- добавлять и удалять продукт в корзину
- формировать заказ
- заполнять shipping-форму для оформления заказа (django-countries)

Приложение позволяет администратору:
- создавать/удалять/изменять категории товаров
- создавать/удалять/изменять наименования товаров внутри категории
- добавлять к каждому товару описание, фотографию, плашки "best seller" либо "new"
- устанавливать скидки от первоначальной цены для каждого товара
- создавать/удалять/изменять заказы внутри корзины

Приложение содержит следущие энд-пойнты:
- /admin/ -панель администратора
- /product/<pk>/ - карточка товара
- /order-summary/ - список выбранных товаров внутри корзины
- /checkout/ - форма для отправки товара

![Вход на сайт](/screenshots/main2.png)
![ВКарточка товара](/screenshots/product.png)
![Корзина](/screenshots/order.png)
![Форма отправки](/screenshots/checkout.png)


Чтобы скопировать проект и запустить его у себя:

1. Создайте виртуальное окружение в папке, куда планируете скачать проект: python -m venv
(например, python -m venv C:\Users\project)

2. Активируйте виртуальное окружение командой cd C:\Users\project\Scripts\activate.bat

3. Скачайте проект по ссылке https://github.com/iren-coder/Django_Ecommerce_Mobile_shop либо склонируйте репозиторий git@github.com:iren-coder/Django_Ecommerce_Mobile_shop.git.

4. Создайте суперпользователя python manage.py createsuperuser

5. Создайте и примините миграции:
python manage.py makemigrations
python manage.py migrate

6. Скопируйте статические файлы python manage.py collectstatic

7. Теперь можно запустить сервер python manage.py runserver
