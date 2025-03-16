﻿# test_Tehnezis
# Настройка проекта
## Клонирование репозитория
```` git clone https://github.com/Ba1Kerrr/test_Tehnezis.git ````

## Переход в директорию проекта
```` cd test_Tehnezis ````

## Создание виртуальной среды
```` python -m venv venv ````

## Активация виртуальной среды:
### Для Linux/MacOS:
```` source venv/bin/activate ````
### Для Windows:
```` venv\Scripts\activate ````

## Установка зависимостей
```` pip install -r requirements.txt ````

## Запуск проекта
```` python main.py ````


# ТЗ

### Представьте, что у вас есть система без интерфейса пользователя, например краулер
(сборщик информации), который парсит все сайты по продаже зюзюбликов и сохраняет в
базу данных.

Появилась потребность дать обычному пользователю минимальными усилиями
добавлять еще сайты для парсинга

##Напишите простого бота, который будет иметь одну кнопку: загрузить файл
1. При нажатии кнопки пользователь прикрепляет файл excel в формате таблицы с
полями:
      a. title - название
      b. url - ссылка на сайт источник
      c. xpath - путь к элементу с ценой
3. Бот получает файл, сохраняет
4. Открывает файл библиотекой pandas
5. Выводит содержимое в ответ пользователю
6. Сохраняет содержимое в локальную БД sqlite


Внутри репозитория должна быть инструкция по развёртыванию и корректный файл с
необходимыми зависимостями (requirements, pipenv, poetry на ваш выбор)
Задание рассчитано на один день, выполнять можно в удобное время в течение недели
