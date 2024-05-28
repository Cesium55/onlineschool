# Используйте официальный образ Python как базовый
FROM python:3.10

# Установите рабочую директорию в контейнере
WORKDIR /app

# Скопируйте файлы проекта в контейнер
COPY . /app

# Установите зависимости
RUN pip install -r requirements.txt

# Запустите сервер разработки Django на порту 8001
CMD ["python", "manage.py", "runserver", "0.0.0.0:8001"]
