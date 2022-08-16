# Тестовое задание: Загрузка данных в БД из CSV

## Содержание
***
  1. [Содержание](#Содержание)
  2. [Введение](#Введение)
  3. [Задание](#Задание)
  4. [Документация](#Документация)
  5. [LICENSE](#LICENSE)

## Введение
***
Данный проект создан по тестовому заданию компании "ООО Пикассо Софт", задание изложено ниже. 

Описание выполненной работы вы найдете в [Документации](#Документация) в разделе "[Отчет о выполненной работе](docs/work_report.md)"

## Задание
***
1. Скачайте реестр обращений в полицию San Francisco, ~335mb
2. Создайте структуру базы данных
3. Напишите python-скрипт, загружающий данные из csv в базу данных.

Скрипт должен отображать процесс загрузки и в результате отобразить кол-во созданных записей и потраченное время.

### Результат
***
Создайте Gist или репозиторий, в котором будут размещены:

1. SQL для создания схемы базы данных
2. Скрипт для загрузки данных
3. Файл с указанием зависимостей
4. LOG-файл с выводом результата работы скрипта

### API
***
Разработайте API, будет возвращать инциденты из базы данных. Необходима фильтрация по Report Date (параметры date_from и date_to) и возможность ограничивать кол-во результатов по 20 шт. на страницу (параметр page)

> [Оригинал задания](https://gist.github.com/tm-minty/c39f9ab2de1c70ca9d4d559505678234) — © 2022 ООО "**_Пикассо Софт_**"

## Документация
***
### 1. [Отчет о выполненной работе](docs/work_report.md)
### 2. [Быстрый старт: Сборка и запуск программы](docs/quick_start.md)


## LICENSE
***

The MIT License (MIT)

Copyright © 2022 Daniil Kvartalnov (dan.kvartalnov@gmail.com)

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.