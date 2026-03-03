from pathlib import Path
import environ

env = environ.Env(
    DEBUG=(bool, False),
    SECRET_KEY=(str, "12345"),
    DB_URL=(str, "sqlite:///db.sqlite3"),
)

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = env("DEBUG")

SECRET_KEY = env("SECRET_KEY")

ALLOWED_HOSTS = []

INSTALLED_APPS = [
    "django.contrib.contenttypes",
    "rest_framework",
    "core",
    "maps",
]

MIDDLEWARE = [
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "core.urls"

WSGI_APPLICATION = "core.wsgi.application"

DATABASES = {
    "default": env.db("DB_URL")
}

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"


REST_FRAMEWORK = {
    "UNAUTHENTICATED_USER": None,
    "DEFAULT_RENDERER_CLASSES": (
        "rest_framework.renderers.JSONRenderer",
    ),
}