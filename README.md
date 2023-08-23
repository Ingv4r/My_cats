# Деплой проектов на удаленный сервер Linux ubuntu
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Linux](https://img.shields.io/badge/Linux-FCC624?style=for-the-badge&logo=linux&logoColor=black)
## Описание проектов
Kittygram - это проект, на котором люди могут делиться с другими своими кошками. Можно регистрироваться, загружать картинки, описывать внешность, имя и достижения своих котиков. 

Taski - площадка, где можно вести свои задачи, описывать их и следить за ходом выполнения.
# Настройка SSH для дотупа к удаленному серверму
## Переход в закрытую директорию .ssh и создание директории для ssh ключей
```
cd ~/.ssh
mkdir название-директории

```
## Установление прав доступа к ssh ключам
Устанавливаем права доступа для файла закрытого SSH-ключа: владелец файла может читать и редактировать его, для других пользователей доступ к файлу закрыт.
```
chmod 600 название_файла_закрытого_SSH-ключа
```
Устанавливаем права доступа для файла открытого SSH-ключа: владелец файла может читать и редактировать его, остальные пользователи — только читать.
```
chmod 644 название_файла_открытого_SSH-ключа.pub
```
# Подключение к удаленному серверу
Ключ -i позволяет указать путь до SSH-ключа, отличный от пути по умолчанию.
```
ssh -i путь_до_файла_с_SSH_ключом/название_файла_закрытого_SSH-ключа login@ip(серевера)
```
Далее нужно ввести пароль от закрытого SSH-ключа (passphrase)
# Запуск backend
```
git clone git@github.com:Ingv4r/infra_sprint1.git
```
```
cd infra_sprint
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
# Запуск frontend
## Установка на сревре пакетного менеджера npm
```
curl -fsSL https://deb.nodesource.com/setup_18.x | sudo -E bash - &&\
sudo apt-get install -y nodejs
```
## Установка зависимостей для frontend
```
cd taski/frontend
npm i
```
