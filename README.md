# Test project

### Выбор инструментов

* Django + Django Rest Framework -
Выбор был между Flask и Django, решил использовать Django, тк было больше опыта работы с ним + удобные дженерики. 

* Celery -
Используется для асинхронного вызова тасок (таска = пуш сообщения в мессенджер). 

* Redis -
В качестве брокера для селери выбрал редис, тк как нужные функции из ТЗ он поддерживает + есть опыт работы с ним

* SQLite -
Проект достаточно простой в плане требований к БД, хватило локальной БД


### Деплой
Проект разворачивается под докером, сценарий развертывания лежит в [docker-comppose.yml](https://github.com/ssalamatov/project404/blob/master/docker-compose.yml), для запуска достаточно будет запустить [setup.sh](https://github.com/ssalamatov/project404/blob/master/setup.sh) (лежит в корне проекта), он развернет 3 контейнера с django-сервером, редисом и селери, подтянет зависимости из [requirements.txt](https://github.com/ssalamatov/project404/blob/master/requirements.txt) и запустит тестовый сервер ```0.0.0.0:8000```.


### Пример использования:
```
curl -i -X POST -H 'Content-Type: application/json' "http://127.0.0.1:8000/messages/" -d '[{"user_id": 123, "messenger_id": 1, "text": "hello", "start_at": "2019-11-26 11:43:10"}, {"user_id": 456, "messenger_id": 0, "text": "hello again"}]'
```

В примере выше делается POST-запрос, в теле списком передаются сообщения для пуша, для отложенных сообщений необходимо указывать ```start_at``` поле с временем отправки, связка ```('user_id', 'messenger_id', 'text')``` должна быть уникальной для избежания дублирования сообщений.


### Документация
Описание спецификации сделано в формате OpenAPI, можно посмотреть в файле [openapi.json](https://github.com/ssalamatov/project404/blob/master/docs/openapi.json)


### Особенности:
В конфиг добавил ключ ```CELERY_NUMBER_RETRIES```, через него указывается кол-во повторений для сфэйленных тасок.
