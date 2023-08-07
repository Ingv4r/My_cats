# API YaMDb
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
## Описание проектов
Kittygram - это проект, на котором люди могут делиться с другими своими кошками. Можно регистрироваться, загружать картинки, описывать внешность, имя и достижения своих котиков. 

Taski - площадка, где можно вести свои задачи, описывать их и следить за ходом выполнения.
## Запуск проекта
```
git clone https://github.com/Ingv4r/api_yamdb
```
```
cd api_yamdb
```
- Cоздать и активировать виртуальное окружение
```
python -m venv venv # Для Windows
python3 -m venv venv # Для Linux и macOS
```
```
source venv/Scripts/activate # Для Windows
source venv/bin/activate # Для Linux и macOS
```
- Установите зависимости из файла requirements.txt
```
pip install -r requirements.txt
``` 
- Перейти в папку со скриптом управления и выполнить миграции
```
cd api_yamdb
```
```
python manage.py migrate
```

- Запустить проект
```
python manage.py runserver
```
## Копирование в базу данных из csv файлов
- В директории с файлом manage.py выполнить команду
```
python manage.py csv_to_bd
```
## Создание суперпользователя
- В директории с файлом manage.py выполнить команду
```
python manage.py createsuperuser
```
- Заполнить поля в терминале
```
Username: <ваше_имя>
Email address: <ваш_email>
Password: <ваш_пароль>
Password (again): <ваш_пароль>
```
## Регистрация нового пользователя
- Передать на эндпоинт 127.0.0.1:8000/api/v1/auth/signup/ **username** и **email**
- Получить код подтверждения на переданный **email**. Права доступа: Доступно без токена. Использовать имя 'me' в качестве **username** запрещено. Поля **email** и **username** должны быть уникальными. 

## Получение JWT-токена
- Передать на эндпоинт 127.0.0.1:8000/api/v1/auth/token/ **username** и **confirmation** code из письма. Права доступа: Доступно без токена.

## Примеры запросов
- Отправить POST-запрос на адрес http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/ и передать поле text и поле score <br>
Пример запроса на создание отзыва: 
```
{
"text": "Отзыв на произведение",
"score": 5
}
```
Пример ответа: 
```
{
"id": 0,
"text": "Отзыв на произведение",
"author": "voronovsv",
"score": 5,
"pub_date": "2019-08-24T14:15:22Z"
}
```
- Отправить POST-запрос на адрес http://127.0.0.1:8000/api/v1/titles/{title_id}/reviews/{review_id}/comments/ и передать поле text <br>
Пример запроса на создание комментария к отзыву:
```
{
"text": "Классный отзыв!"
}
```
Пример ответа:
```
{
"id": 0,
"text": "Классный отзыв!",
"author": "string",
"pub_date": "2019-08-24T14:15:22Z"
}
```
## Полная документация к API проекта:

Перечень запросов к ресурсу можно посмотреть в описании API

```
http://127.0.0.1:8000/redoc/
```
## Над проектом работали
<br>Врач</br>
<br>1Сник</br>
<br>Студент, вчерашний выпускник</br>
