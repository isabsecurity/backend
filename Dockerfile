# Python 3.12 bazaviy imidj
FROM python:3.12-slim

# Ishchi papka
WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# requirements.txt faylini nusxalab, kutubxonalarni o'rnatamiz
RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Butun loyiha fayllarini konteynerga ko‘chiramiz
COPY . .
EXPOSE 8000
# Django runserver va Telegram botni bir vaqtda ishga tushiramiz
CMD ["sh", "-c", "python manage.py collectstatic --noinput && gunicorn config.wsgi:application --bind 0.0.0.0:8000 --workers 3 & python manage.py bot & wait"]
