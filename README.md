**Приложение (чат-бот) для отображения актуального курса валют.**

  Сервис ужедневно получает XML файл с курсами валют с сайта Центрального банка России (ЦБ РФ)
Обновляет данные в Redis.
Сервис бота:

Отвечает на команду /exchange, например: /exchange USD RUB 10 и отображает стоимость 10 долларов в рублях.
Отвечает на команду /rates, отправляя пользователю актуальные курсы валют.

разработан с помощью:
1. Aiogram
2. Redis
3. Celery
4. aiohttp

Celery служит для ежедневного обновления курса валют, периодичность обновлений задаётся в файле .env

***запуск***

Для запуска потребуется создать в корневой папке файл .env со следующими переменными: 
1. BOT_TOCKEN
2. REDIS_PORT
3. REDIS_HOST
4. REDIS_PASSWORD
5. REDIS_USER
6. REDIS_USER_PASSWORD
7. CELERY_TIME_UPDADE

CELERY_TIME_UPDADE - частота обновлений курса валют, задаётся в сек.

Для запуска потребуется docker, билдим, запускаем. 
1. переходим в директорию где лежит файл docker-compose.yaml
2. docker compose build [OPTIONS] [SERVICE...]
3. docker compose up [OPTIONS] [SERVICE...]


**Бот @test_test_ukolov_bot**

