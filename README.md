### Коротко о проекте:

предоставляет API интерфейс основанный на Django REST framework. Позволяет: 
```
- создать, просмотривать, редактировать посты.
- создавать, просматривать, редактировать комментарии к постам. Доступен просмотр незарегистированным пользователям.
- управлять подписками на интересующих пользователей(доступно только авторизованным пользователям). 
- просматривать информацию о группах
- управлять JWT токенами для авторизованного доступа.
```

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone git@github.com:Intemic/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python3 -m venv env
```

```
source env/bin/activate
```

```
python3 -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python3 manage.py migrate
```

Запустить проект:

```
python3 manage.py runserver
```

Ознакомиться с документацией проекта можно по адресу:

```
http://127.0.0.1:8000/redoc/
```
