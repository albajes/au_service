# Сервис авторизации

## Автор
Альберт Аберхаев

### Возможности:
 - регистрация
 - авторизация
 - получение, обновление и проверка jwt токенов
 - получение списка пользователей
 - добавление и удаление из чс


## Описание проекта:
Все проекты написаны на языке Python с использованием: 
- DRF (Django Rest Framework)
- pcycorpg2
- simplejwt
- celery
- redis
- postgresql
- requests
- docker
- daphne
- channels


# API
- #### Регистрация:  POST /registration/
- > curl --location 'http://127.0.0.1:8000/registration \
--header 'Content-Type: application/json' \
--data '{
    "username": "albert",
    "email": "albert@email.com",
    "password": "albertalbert"
}'

- > Ожидает тело запроса. Пример:
`    {
    "username": "albert",
    "email": "albert@email.com",
    "password": "albertalbert"
}

Возвращает HTTP код в случае успешного создания и ответ: {
    "username": "albert",
    "email": "albert@email.com"
}

Возвращает HTTP код 400 в случае некорректного запроса и тело ответа с описанием ошибки. Пример: { "username": [ "This field is required." ] }

Возвращает HTTP код 400 в случае попытки записать пользователя, имя или почта которого уже есть в базе данных, и тело ответа с описанием ошибки. Пример: { "username": [ " this name already exists." ] }

- #### Авторизация:  POST /login/
- > curl --location 'http://127.0.0.1:8000/login \
--header 'Content-Type: application/json' \
--data '{
    "email": "albert@email.com",
    "password": "albertalbert"
}'

- > Ожидает тело запроса. Пример:
`    {
    "email": "albert@email.com",
    "password": "albertalbert"
}

Возвращает HTTP код 201 в случае успешной авторизации и тело ответа. Пример:{
    "username": "albert",
    "email": "albert@email.com"
}

Возвращает HTTP код 400 в случае некорректного запроса и ответ с описанием ошибки. Пример: Not user with this email and password

- #### Получение списка пользователей:  GET /users/
- > curl --location 'http://127.0.0.1:8000/users/'

Возвращает HTTP код 200 в случае успешного получения данных и тело ответа. Пример:
 { "username": "albert", "email": "albert@email.com"}

- #### Добавить/удалить пользователя из ЧС:  POST /blist/
- > curl --location 'http://127.0.0.1:8000/blist \
--header 'Authorization: JWT eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3Mzg2ODc1LCJpYXQiOjE2OTczODYyNzUsImp0aSI6IjczYTMwNTI2YmY3MjQxNzliNzlmOWYzOTNhZTIzZWExIiwidXNlcl9pZCI6Mn0.lDo0saqwYYElNwzK5tqw8BNYPK4rgU068UkuVpF01LQ' \
--data '{
    "bad_user": 1
}'

В поле "bad_user" указываем id пользователя, которому хотим запретить/разрешить отправлять сообщения.
Нельзя самого себя добавить в ЧС, обязательно тело запроса. Пример: {
    "bad_user": 1
}

Возвращает HTTP код 201 в случае успешного запроса и ответ "Упешно".
Возвращает HTTP код 400 в случае неуспешного запроса и ответ "Вы не можете сами себя добавить в ЧС" или 'Укажите поле "bad_user"'.

- #### Поиск связи пользователей в таблице ЧС: GET /get_blist/1/2
- > curl --location 'http://127.0.0.1:8000/get_blist/<int:good_user>/<int:bad_user>'

Возвращает HTTP код 200 в случае успешного запроса и тело ответа. Пример: {
    "id": 1,
    "good_user": 2,
    "bad_user": 1
}

Возвращает HTTP код 400 в случае неуспешного запроса. 

- #### Получить access token и refresh token: POST /ac_token
- > curl --location 'http://127.0.0.1:8000/ac_token \
--data '{
    "email": "albert@email.com",
    "password": "albertalbert"
}'
- > Ожидает тело запроса. Пример: 
{
    "email": "albert@email.com",
    "password": "albertalbert"
}

Возвращает HTTP код 200 в случае успешного запроса и тело ответа. Пример: "{

"refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY5NTkzMzYwMSwiaWF0IjoxNjk1Njc0NDAxLCJqdGkiOiJmNDc2MGI1Y2Q5ZDk0NzBjODI1ZGE3M2NiODgzNWE5NSIsInVzZXJfaWQiOjR9.5C3IdxpSiJs3reoJ_WUlmQ_XSNjrCrjqkgxX5JcLdp0",

"access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk1Njc1MDAxLCJpYXQiOjE2OTU2NzQ0MDEsImp0aSI6ImVhNzY4N2I1OGJiYTQyMGJiYjM4ZDg5NGE1ODFjOTBlIiwidXNlcl9pZCI6NH0.37qr7icBL-hBtCb1CyCXe63wsJRhp_1R7Ji9UhsZB2s"

}"

- #### Проверка access token: POST /verify
- > curl --location 'http://127.0.0.1:8000/verify \
--data '{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3MTM3OTU2LCJpYXQiOjE2OTcxMzczNTYsImp0aSI6ImJmYzI2OWQ2ZWE0MDQ2M2M5MjY2YzU3ZTRiYWNjZmYwIiwidXNlcl9pZCI6MX0.Jwa1D8VtwfkX_ni3g3jrLn5r9Um-lbGGbthS4XdeGJE"
}'
- > Ожидает тело запроса. Пример: 
{
    "token": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk3MTM3OTU2LCJpYXQiOjE2OTcxMzczNTYsImp0aSI6ImJmYzI2OWQ2ZWE0MDQ2M2M5MjY2YzU3ZTRiYWNjZmYwIiwidXNlcl9pZCI6MX0.Jwa1D8VtwfkX_ni3g3jrLn5r9Um-lbGGbthS4XdeGJE"
}

Возвращает HTTP код 200 в случае успешного запроса.

Возвращает HTTP код 401 в случае неуспешного запроса и тело ответа. Пример: {
    "detail": "Токен недействителен или просрочен",
    "code": "token_not_valid"
}

- #### Обновление access token: POST /re_token
- > curl --location 'http://127.0.0.1:8000/re_token \
--data '{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4OTk3MDU0LCJpYXQiOjE2ODg5OTY4NzQsImp0aSI6IjBkNGIxMTE2MzZmNTRmMjk4ZjI4MTA5YzY0ZjIxYzg3IiwidXNlcl9pZCI6Mn0.IscCofdoAsf8I6m2N-b8l1r8M4HuOlxPtpI2awKpv9c"
}'
- > Ожидает тело запроса. Пример: 
{
    "refresh": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4OTk3MDU0LCJpYXQiOjE2ODg5OTY4NzQsImp0aSI6IjBkNGIxMTE2MzZmNTRmMjk4ZjI4MTA5YzY0ZjIxYzg3IiwidXNlcl9pZCI6Mn0.IscCofdoAsf8I6m2N-b8l1r8M4HuOlxPtpI2awKpv9c"
}

Возвращает HTTP код 200 в случае успешного запроса и тело ответа. Пример: {
    "access": "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjg4OTk3MDU0LCJpYXQiOjE2ODg5OTY4NzQsImp0aSI6IjBkNGIxMTE2MzZmNTRmMjk4ZjI4MTA5YzY0ZjIxYzg3IiwidXNlcl9pZCI6Mn0.IscCofdoAsf8I6m2N-b8l1r8M4HuOlxPtpI2awKpv9c"
}

Возвращает HTTP код 401 в случае неуспешного запроса и тело ответа. Пример: {
    "detail": "Токен недействителен или просрочен",
    "code": "token_not_valid"
}

## Запуск проекта в Docker-контейнере:

Для запуска проекта в Docker-контейнере необходим установленный и запущенный **Docker** на локальной машине.

Необходимо файл docker-compose.yml переместить в ту же дерикторию, где находятся все сервисы (service_1, service2, service_3).
Сейчас он находится в директории /service_1.
Запустить терминал в этой директории и выполнить команду:
`docker-compose build`
`docker-compose up -d`

Подключиться к БД в контейнере Docker можно по следующим настройкам: 

- 'NAME': 'postgres'
- 'USER': 'albert'
- 'PASSWORD': '037700'
- 'HOST': '127.0.0.1'
- 'PORT': '5434'