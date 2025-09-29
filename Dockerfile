# Use official Python image
FROM python:3.12-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy project files
COPY . /app/

# Collect static files (at build time)
RUN python manage.py collectstatic --noinput

# Default command: run migrations, create superuser if needed, then start Gunicorn
CMD bash -c "\
  python manage.py migrate --noinput && \
  python manage.py collectstatic --noinput && \
  echo 'from django.contrib.auth.models import User; import os; \
if not User.objects.filter(username=os.environ.get(\"DJANGO_SUPERUSER_USERNAME\")).exists(): \
    User.objects.create_superuser( \
        os.environ.get(\"DJANGO_SUPERUSER_USERNAME\"), \
        os.environ.get(\"DJANGO_SUPERUSER_EMAIL\"), \
        os.environ.get(\"DJANGO_SUPERUSER_PASSWORD\") \
    )' | python manage.py shell && \
  gunicorn finnmac_site.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 4"
