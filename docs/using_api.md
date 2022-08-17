# Использование API

Для проверки части задания с API, переходим на `http://localhost/api/v1/service-calls`

![API - Service Call List](/docs/images/API_service_call.png "API - Service Call List")

Вы можете добавить GET-параметр `page`, в таком случае будет обеспечен отступ на 20 сущностей

Вы можете использовать параметры `date_after` и `date_before` (вместо `date_from` и `date_to`) для фильтрации по полю `report_date`

> Все сущности изначально отфильтрованы по `report_date`

<br />

> **Пред.**: [Запуск парсера CSV](launch_csv_parser.md)
>
> **Главная**: [README.md](/README.md)