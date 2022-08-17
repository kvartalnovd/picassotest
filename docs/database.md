# База данных: Подключение
Для проверки работы базы данных, после запуска docker'а можно пойти тремя способами:
Подключиться к БД через PgAdmin4, через легкий Adminer или Django Admin

> На прод. версии, данные варианта, естественно, либо были бы заблокированны, либо контроллировались бы высшими силами


## Содержание
  1. [Содержание](#Содержание)
  2. [Первый способ: PgAdmin](#Первый-способ-PgAdmin)
  3. [Второй способ: Adminer](#Второй-способ-Adminer)
  4. [Третий способ: Django admin](#Третий-способ-Django-admin)


## Первый способ: PgAdmin

1. Заходим на `locahost:16543`

2. Вводим логин/пароль: admin@picasso.ru / password

![PgAdmin | login](/docs/images/pgadmin_login.png "PgAdmin | login")

3. Подключаемся к серверу

Вводим любое имя для подключения

![PgAdmin | connection to server | Server > General](/docs/images/pgadmin_add_server.png "PgAdmin | connection to server | Server > General")

Вводим следующие данные:

**Host:** 172.17.0.1 _(IP докера - ваш может отличаться, на wsl2 и ubuntu 20.04 LTS работает корректно)_

**Port:** 5432

**Username:** user

**Password:** password

![PgAdmin | Server > Connection](/docs/images/pgadmin_connection.png "PgAdmin | connection to server | Server > Connection")


4. Profit! Получаем доступ к БД

![PgAdmin | Access to the server was obtained](/docs/images/pgadmin_access.png "PgAdmin | Access to the server was obtained")

## Второй способ: Adminer

Adminer гораздо проще:

1. Заходим на `localhost:8080`
2. Выбираем `PostgreSQL` в качестве движка и вводим следующие данные:

**Сервер:** db

**Имя пользователя:** user

**Пароль:** password

**База данных:** picasso-db

![Adminer | Login](/docs/images/adminer-login.png "Adminer | Login")

3. Получаем доступ к БД

![Adminer | Access to the server was obtained](/docs/images/adminer_access.png "Adminer | Access to the server was obtained")


## Третий способ: Django admin

1. Заходим на `http://localhost/admin`
2. Вводим логин/пароль: **admin** / **admin**

<br />

> **Пред.**: [Быстрый старт: Сборка и запуск программы](quick_start.md)
>
> **Главная**: [README.md](/README.md)
> 
> **Далее**: [Запуск парсера CSV](launch_csv_parser.md)