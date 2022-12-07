[![Python](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://www.python.org/downloads/release/python-396/)
[![Scrapy](https://img.shields.io/badge/-Python-464646?style=flat&logo=Python&logoColor=ffffff&color=043A6B)](https://scrapy.org/)

# Асинхронный парсер PEP

Парсер документов PEP на базе фреймворка Scrapy. Парсер создает два файла отчета: файл со списком PEP, включающим номер документа, название и статус, и файл суммарной статистики по количеству документов в разных статусах.

## Запуск парсера на macOS

1. Клонируйте репозиторий:  
`git clone git@github.com:Hastred45/bs4_parser_pep.git`
2. Создайте и активируйте виртуальное окружение:  
`python3 -m venv venv`  
`source venv/bin/activate`  
3. Установите зависимости:  
`pip install -r requirements.txt`
4. Запустите парсер:  
`scrapy crawl pep`

## Автор

Сергей Осетров