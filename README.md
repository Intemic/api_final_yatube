## Коротко о проекте:

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

### Примеры запросов:

**GET** api/v1/posts/
```
{
  "count": 123,
  "next": "http://api.example.org/accounts/?offset=400&limit=100",
  "previous": "http://api.example.org/accounts/?offset=200&limit=100",
  "results": [
    {
      "id": 0,
      "author": "string",
      "text": "string",
      "pub_date": "2021-10-14T20:41:29.648Z",
      "image": "string",
      "group": 0
    }
  ]
}
```

**GET** api/v1/posts/{post_id}/comments/
```
[
  {
    "id": 0,
    "author": "string",
    "text": "string",
    "created": "2019-08-24T14:15:22Z",
    "post": 0
  }
]
```

**POST** api/v1/posts/{post_id}/comments/
```
{
"text": "string"
}

Response:

{
  "id": 0,
  "author": "string",
  "text": "string",
  "created": "2019-08-24T14:15:22Z",
  "post": 0
}

```

... 
для более полной информации обратитесь к документации
