# Dockerfile
FROM python:3.10-slim
LABEL authors="Panfilov Valerian"

# Устанавливаем зависимости для сборки MySQL клиента
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    pkg-config \
    libmariadb-dev

# Установка рабочей директории
WORKDIR /app

# Устанавливаем pip
RUN pip install --upgrade pip
COPY requirements.txt requirements.txt
RUN pip install -r /app/requirements.txt

# Копирование кода приложения
COPY . .



# Запуск команды для старта сервера
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]



