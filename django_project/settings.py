from pathlib import Path
from django.core.management.utils import get_random_secret_key
from environs import Env

env = Env()
env.read_env()

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-SECRET_KEY
SECRET_KEY = env.str("SECRET_KEY", get_random_secret_key())

# https://docs.djangoproject.com/en/dev/ref/settings/#debug
DEBUG = env.bool("DEBUG", False)

# https://docs.djangoproject.com/en/dev/ref/settings/#allowed-hosts
ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

# https://docs.djangoproject.com/en/dev/ref/settings/#installed-apps
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "whitenoise.runserver_nostatic",
    "django.contrib.staticfiles",
    "django.contrib.sites",
    # Third-party
    "allauth",
    "allauth.account",
    "crispy_forms",
    "crispy_bootstrap5",
    # Local
    "accounts",
    "pages",
]


# https://docs.djangoproject.com/en/dev/ref/settings/#middleware
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # WhiteNoise
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
    "allauth.account.middleware.AccountMiddleware",  # django-allauth
]

if DEBUG:
    INSTALLED_APPS += ["django_extensions","debug_toolbar"]
    MIDDLEWARE += ["debug_toolbar.middleware.DebugToolbarMiddleware",]  # Django Debug Toolbar


# https://docs.djangoproject.com/en/dev/ref/settings/#root-urlconf
ROOT_URLCONF = "django_project.urls"

# https://docs.djangoproject.com/en/dev/ref/settings/#wsgi-application
WSGI_APPLICATION = "django_project.wsgi.application"

# https://docs.djangoproject.com/en/dev/ref/settings/#templates
TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

# https://docs.djangoproject.com/en/dev/ref/settings/#databases
default_dburl = "sqlite:///" + str(BASE_DIR / "db.sqlite3")
DATABASES = {"default": env.dj_db_url("DATABASE_URL", default=default_dburl)}

# https://docs.djangoproject.com/en/dev/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# https://docs.djangoproject.com/en/dev/topics/i18n/
# https://docs.djangoproject.com/en/dev/ref/settings/#language-code
LANGUAGE_CODE = env.str("LANGUAGE_CODE","en-us")

# https://docs.djangoproject.com/en/dev/ref/settings/#time-zone
TIME_ZONE = env.str("TIME_ZONE", "UTC")

# https://docs.djangoproject.com/en/dev/ref/settings/#std:setting-USE_I18N
USE_I18N = True

# https://docs.djangoproject.com/en/dev/ref/settings/#use-l10n
USE_L10N = True

# https://docs.djangoproject.com/en/dev/ref/settings/#use-tz
USE_TZ = True

# https://docs.djangoproject.com/en/dev/ref/settings/#static-root
STATIC_ROOT = BASE_DIR / "staticfiles"

# https://docs.djangoproject.com/en/dev/ref/settings/#static-url
STATIC_URL = "/static/"

# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#std:setting-STATICFILES_DIRS
STATICFILES_DIRS = [BASE_DIR / "static"]

# https://whitenoise.readthedocs.io/en/latest/django.html
STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# django-crispy-forms
# https://django-crispy-forms.readthedocs.io/en/latest/install.html#template-packs
CRISPY_TEMPLATE_PACK = "bootstrap5"

# https://docs.djangoproject.com/en/dev/ref/settings/#email-backend
EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"

# django-debug-toolbar
# https://django-debug-toolbar.readthedocs.io/en/latest/installation.html
# https://docs.djangoproject.com/en/dev/ref/settings/#internal-ips
INTERNAL_IPS = ["127.0.0.1"]

# https://docs.djangoproject.com/en/dev/topics/auth/customizing/#substituting-a-custom-user-model
AUTH_USER_MODEL = "accounts.CustomUser"

# django-allauth config
# https://docs.djangoproject.com/en/dev/ref/settings/#site-id
SITE_ID = 1

# https://docs.djangoproject.com/en/dev/ref/settings/#login-redirect-url
LOGIN_REDIRECT_URL = env.str('LOGIN_REDIRECT_URL', "home")

# https://django-allauth.readthedocs.io/en/latest/views.html#logout-account-logout
ACCOUNT_LOGOUT_REDIRECT_URL = env.str("ACCOUNT_LOGOUT_REDIRECT_URL", "home")

# https://django-allauth.readthedocs.io/en/latest/installation.html?highlight=backends
AUTHENTICATION_BACKENDS = (
    "django.contrib.auth.backends.ModelBackend",
    "allauth.account.auth_backends.AuthenticationBackend",
)
# https://django-allauth.readthedocs.io/en/latest/configuration.html
ACCOUNT_SESSION_REMEMBER = env.bool("ACCOUNT_SESSION_REMEMBER", True)
ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE = env.bool("ACCOUNT_SIGNUP_PASSWORD_ENTER_TWICE", False)
ACCOUNT_USERNAME_REQUIRED = env.bool("ACCOUNT_USERNAME_REQUIRED", False)
ACCOUNT_AUTHENTICATION_METHOD = env.str("ACCOUNT_AUTHENTICATION_METHOD","email")
ACCOUNT_EMAIL_REQUIRED = env.bool("ACCOUNT_EMAIL_REQUIRED", True)
ACCOUNT_UNIQUE_EMAIL = env.bool("ACCOUNT_UNIQUE_EMAIL", True)

SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
SECURE_SSL_REDIRECT = True


import os

LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "handlers": {
        "console": {
            "level": "DEBUG",
            "class": "logging.StreamHandler",
        },
    },
     'loggers': {
        'werkzeug': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': True,
        },
     },
}

# Truncate SQL queries to this many characters (None means no truncation)
RUNSERVER_PLUS_PRINT_SQL_TRUNCATE = 1000

# After how many seconds auto-reload should scan for updates in poller-mode
RUNSERVERPLUS_POLLER_RELOADER_INTERVAL = 1

# Werkzeug reloader type [auto, watchdog, or stat]
RUNSERVERPLUS_POLLER_RELOADER_TYPE = 'auto'

# Add extra files to watch
RUNSERVER_PLUS_EXTRA_FILES = []

# Do not watch files matching any of these patterns
RUNSERVER_PLUS_EXCLUDE_PATTERNS = []
