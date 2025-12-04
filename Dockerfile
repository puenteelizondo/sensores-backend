FROM python:3.11-slim

ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

WORKDIR /app

# Dependencias del sistema
RUN apt-get update && apt-get install -y \
    gcc \
    python3-dev \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements DESDE LA RAIZ
COPY requirements.txt /tmp/requirements.txt

# Instalar dependencias Python
RUN pip install --no-cache-dir -r /tmp/requirements.txt

# Copiar entrypoint
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

# Copiar el código Django
COPY app/ /app/

EXPOSE 8000

ENTRYPOINT ["/entrypoint.sh"]
