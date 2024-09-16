# Используем официальный образ Python
FROM python:3.12.4-slim

# Устанавливаем рабочую директорию внутри контейнера
WORKDIR /app

# Копируем файл зависимостей в контейнер
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект в контейнер
COPY . .

# Открываем порт 8000 для доступа к приложению
EXPOSE 8005

# Команда для запуска приложения
CMD ["python", "manage.py", "runserver", "0.0.0.0:8005"]

