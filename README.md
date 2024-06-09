# DobrinSite

DobrinSite_v1 - это веб-сайт для картинной галереи Николая Добрина, разработанный на Python с использованием Django. Проект также использует Docker для контейнеризации, что упрощает развертывание и управление зависимостями.

## Содержание

- [Установка](#установка)
- [Использование](#использование)
- [Структура проекта](#структура-проекта)
- [Вклад](#вклад)
- [Лицензия](#лицензия)

## Установка

### Предварительные требования

Перед началом установки убедитесь, что у вас установлены следующие компоненты:

- [Docker](https://www.docker.com/get-started)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Шаги установки

1. Клонируйте репозиторий на ваш локальный компьютер:
    ```bash
    git clone https://github.com/SharkDeveloper/DobrinSite_v1.git
    cd DobrinSite_v1
    ```

2. Создайте файл `.env` в корне проекта и настройте переменные окружения, если это необходимо:

## Использование

### Использование Docker

1. Соберите и запустите контейнеры Docker:
    ```bash
    docker-compose up --build --no-cache
    ```

2. Примените миграции базы данных:
    ```bash
    docker-compose exec web python manage.py migrate
    ```

3. Создайте суперпользователя для доступа к админ-панели Django:
    ```bash
    docker-compose exec web python manage.py createsuperuser
    ```

4. Откройте веб-браузер и перейдите по адресу [http://127.0.0.1:8000](http://127.0.0.1:8000).

## Структура проекта

```plaintext
DobrinSite_v1/
├── app/
│   ├── static/
│   ├── templates/
│   ├── __init__.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
│   ├── settings.py
│   ├── wsgi.py
│   └── asgi.py
├── migrations/
├── tests/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
├── .env
├── manage.py
└── README.md
```

app/ - Каталог с исходным кодом приложения.  
static/ - Статические файлы (CSS, JS, изображения).  
templates/ - HTML шаблоны.  
__init__.py - Инициализация приложения.  
models.py - Модели базы данных.  
urls.py - Маршруты приложения.  
views.py - Представления приложения.  
settings.py - Настройки Django.  
wsgi.py - WSGI конфигурация для развертывания.  
asgi.py - ASGI конфигурация для развертывания.  
migrations/ - Каталог для миграций базы данных.  
tests/ - Каталог с тестами.  
Dockerfile - Docker файл для сборки образа.  
docker-compose.yml - Конфигурация Docker Compose.  
requirements.txt - Зависимости проекта.  
.env - Файл с переменными окружения.  
manage.py - Командный файл Django.  
README.md - Документация проекта.  

## Вклад
Мы приветствуем вклад в проект! Если вы хотите внести свой вклад, пожалуйста, следуйте следующим шагам:

Форкните репозиторий.
Создайте новую ветку для вашей фичи (git checkout -b feature/YourFeature).
Внесите изменения и сделайте коммит (git commit -am 'Add YourFeature').
Запушьте изменения в ваш форк (git push origin feature/YourFeature).
Создайте Pull Request на рассмотрение.

## Лицензия
Этот проект лицензируется под лицензией MIT. Подробнее см. в файле LICENSE.
