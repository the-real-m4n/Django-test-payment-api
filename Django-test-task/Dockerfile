# Основной образ с Python
FROM python:3.9-slim

# Установка зависимостей для сборки (если нужны)
RUN apt-get update && apt-get install -y --no-install-recommends gcc && apt-get clean && rm -rf /var/lib/apt/lists/*

# Создаем рабочую директорию
WORKDIR /app

# Копируем файлы проекта в контейнер
COPY . /app

# Устанавливаем зависимости из requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Собираем статические файлы (если используешь collectstatic)
#RUN python manage.py collectstatic --no-input

# Запускаем сервер разработки (для production используй gunicorn или другого веб-сервера)
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]