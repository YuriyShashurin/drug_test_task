# drug_test_task
## Тестовое задание для Backend-разработчиков платформы ДРУГ

Задание: https://docs.google.com/document/d/1XhRL049wCGvQA3q6BMGBRfH2346pJFf2GcbEiHqnixg/edit#heading=h.sfwrxtt3ddsa

### Stack реализации backend проекта:
* Python 3.10
* фрейворк FastApi + PostgreSql 13

### Как развернуть проект локально

#### 1. Cклонировать данный репозиторий

```
git clone https://github.com/YuriyShashurin/drug_test_task.git
```

#### 2. Перейти в папку проекта

```
cd drug_test_task
```

#### 3. Создать виртуальное окружение (вводим команду в командной строке из папки проекта)
```
* python -m venv venv
```

#### 4. Создаем файл .env в папке drug_test_task/app и добавляем актуальные для вас значения переменных окружения ниже
```
POSTGRES_DB="ENTER_YOUR_SECRET_KEY"
POSTGRES_NAME="postgres"
POSTGRES_HOST="localhost"
POSTGRES_PASSWORD="enter_your_password"
POSTGRES_PORT=5312
```
#### 4.1 Запускаем файл run.bat (Для Windows) или makefile(для Linux, не проверялось) из корневой папки проекта. После этого устанавливаются зависимости проекта, а также запускается проект на локальном сервисе по адресу:
```
http://127.0.0.1:8080/
```
#### 4.2 Альтернативный вариант запуска. В консоле из корневой папки проекта вводим по очереди команды:
```
venv\Scripts\activate.bat
```
```
pip install -r requirements.txt
```
```
uvicorn setup:app --reload --port 8080
```

#### 5 После запуска проекта сразу скрипт создаст БД в PostgreSql(согласно указаному имени в .env) и добавит таблицы из схемы БД файла create_tables.sql (в корне проекта)


#### 6 Открыть проект по ссылке
```
http://127.0.0.1:8080
```

### Документация методов API проекта:
```
http://127.0.0.1:8080/docs
```

### Эндпойты методов API
#### 1. Обработка регистрационных данных + валидация и сохранение в БД. Метод POST. Принимает на вход JSON объект, Возвращает json с идентификатором пользователя в случае успеха, в случае ошибки возвращает json с двумя полями Код и Сообщения
```
http://127.0.0.1:8080/v1/auth/register/
```
#### 2. Обработка логина и пароля для лог ина: валидация и поиск в БД. Метод POST. принимает json с логином паролем и возвращает json с идентификатором пользователя и статусом аутентификации в случае успеха, в случае ошибки возвращает json с двумя полями Код и Сообщение
```
http://127.0.0.1:8080/v1/auth/login/
```

#### 3. Обработка для лог аута. Метод POST. Принимает json с айди. Возвращает json с идентификатором пользователя и статусом аутентификации в случае успеха, в случае ошибки возвращает json с двумя полями Код и Сообщение
```
http://127.0.0.1:8080/v1/auth/logout/
```

#### 4. Обработка получения информации о пользователе. Метод GET с query-параметром id, возвращает json со всеми полями пользователя (кроме пароля) или Код-Текст ошибки 
```
http://127.0.0.1:8080/v1/user?id={{id}}
```

### Дополнительно реализовано(по сравнению с заданием):
* Метод обработки для лог аута. Выход из системы пользователем.
* Помимо айди, в запросах возвращается статус аутентификации для последующей обработки на фронтенде
* Айди пользователю присваивается в uuid4 формате, чтобы избежать варианты подбора айди
* Получение данных для GET запроса доступно только аутенцифицированным пользователям (те, у которых "is_authenticated": true). Иначе возвращается ошибка. ToDo: сделать формирование токенов с сроком действия и использование их в GET запросов для получения данных
* Настроен логгер crud методов API
