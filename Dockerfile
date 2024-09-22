# Используем официальный образ Python
FROM python:3.12.4-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt .

RUN pip install gunicorn

RUN apt-get update && apt-get install -y netcat-openbsd && rm -rf /var/lib/apt/lists/*
# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект в контейнер
COPY . .

# Открываем порт 8000 для доступа к приложению
EXPOSE 8005

# Команда для запуска приложения
CMD ["./entrypoint.sh", "db", "5432"]

