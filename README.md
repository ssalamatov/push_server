# Push server

### Стэк

* Django Rest Framework, Celery.

### Деплой
Проект разворачивается под докером, сценарий развертывания лежит в [docker-comppose.yml](https://github.com/ssalamatov/project404/blob/master/docker-compose.yml), для запуска достаточно будет запустить [setup.sh](https://github.com/ssalamatov/project404/blob/master/setup.sh) (лежит в корне проекта), он развернет 3 контейнера с django-сервером, редисом и селери, подтянет зависимости из [requirements.txt](https://github.com/ssalamatov/project404/blob/master/requirements.txt) и запустит тестовый сервер ```0.0.0.0:8000```.
Если селери не сможет подключиться к редису, то нужно поправить адрес подключения (параметр ```CELERY_BROKER_URL``` из [settings.py](https://github.com/ssalamatov/project404/blob/master/project404/settings.py))


### Пример использования:
```
curl -i -X POST -H 'Content-Type: application/json' "http://127.0.0.1:8000/messages/" -d '[{"user_id": 123, "messenger_id": 1, "text": "hello", "start_at": "2019-11-26 11:43:10"}, {"user_id": 456, "messenger_id": 0, "text": "hello again"}]'
```

В примере выше делается POST-запрос, в теле списком передаются сообщения для пуша, для отложенных сообщений необходимо указывать ```start_at``` поле с временем отправки, связка ```('user_id', 'messenger_id', 'text')``` должна быть уникальной для избежания дублирования сообщений.

Пример с дублированием:
```
❯ curl -s -X POST -H 'Content-Type: application/json' "http://127.0.0.1:8000/messages/" -d '[{"user_id": 123, "messenger_id": 1, "text": "deq"},{"user_id": 123, "messenger_id": 1, "text": "1"}]' | jq '.'
[
  {
    "non_field_errors": [
      "The fields user_id, messenger_id, text must make a unique set."
    ]
  },
  {
    "non_field_errors": [
      "The fields user_id, messenger_id, text must make a unique set."
    ]
  }
]
``` 


### Документация
Описание спецификации сделано в формате OpenAPI, можно посмотреть в файле [openapi.json](https://github.com/ssalamatov/project404/blob/master/docs/openapi.json)
