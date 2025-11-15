# -----------------------------
# Base Python Image
# -----------------------------
FROM python:3.12-slim

# Prevent Python from buffering stdout & writing .pyc files
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set working directory
WORKDIR /app

# -----------------------------
# System Dependencies (required for Pillow + psycopg2)
# -----------------------------
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    libfreetype6-dev \
    && rm -rf /var/lib/apt/lists/*

# -----------------------------
# Install Python dependencies
# -----------------------------
COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

# -----------------------------
# Copy project files
# -----------------------------
COPY . /app/

# -----------------------------
# Collect static files at build time
# -----------------------------
RUN python manage.py collectstatic --noinput

# -----------------------------
# Entrypoint: migrate + start Gunicorn
# -----------------------------
CMD bash -c "\
    echo '🚀 Running migrations...' && \
    python manage.py migrate --noinput && \
    echo '📦 Collecting static files...' && \
    python manage.py collectstatic --noinput && \
    echo '👑 Ensuring superuser...' && \
    python manage.py ensure_superuser && \
    echo '🔥 Starting Gunicorn...' && \
    gunicorn finnmac_site.wsgi:application --bind 0.0.0.0:${PORT:-8000} --workers 4 \
"
