# Use the official Python slim image
FROM python:3.13-slim-bookworm

# Set environment variables to prevent Python from writing .pyc files to disk
# and to buffer stdout and stderr
ENV PYTHONDONTWRITEBYTECODE=1 PYTHONUNBUFFERED=1

# Create warpy user and app directory
RUN useradd -m warpy && mkdir -p /app && chown -R warpy:warpy /app

# Set the working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt && pip install gunicorn psycopg2-binary

# Copy the Django project
COPY --chown=warpy:warpy core /app/core
COPY --chown=warpy:warpy maps /app/maps
COPY --chown=warpy:warpy manage.py /app/manage.py

# Switch to the warpy user
USER warpy

# Expose port 8000 for the Django app
EXPOSE 8000

# Run the Gunicorn server
CMD ["gunicorn", "--workers", "2", "--bind", "0.0.0.0:8000", "core.wsgi:application"]