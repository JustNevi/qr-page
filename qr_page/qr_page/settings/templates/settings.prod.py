import json

DEBUG = False
SECRET_KEY = os.getenv(f"{ENV_VARS_SETTINGS_PREFIX}SECRET_KEY")

# Enable corsheaders for local tests

INSTALLED_APPS.append("corsheaders")

CORS_ALLOWED_ORIGINS = json.loads(os.getenv(f"{ENV_VARS_SETTINGS_PREFIX}ALLOWED_ORIGINS"))

# Put CorsMiddleware before CommonMiddleware
common_middleware_index = MIDDLEWARE.index("django.middleware.common.CommonMiddleware")
MIDDLEWARE.insert(common_middleware_index, "corsheaders.middleware.CorsMiddleware")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': os.getenv(f"{ENV_VARS_SETTINGS_PREFIX}DATABASE_NAME"),
        'USER': os.getenv(f"{ENV_VARS_SETTINGS_PREFIX}DATABASE_USER"),
        'PASSWORD': os.getenv(f"{ENV_VARS_SETTINGS_PREFIX}DATABASE_PASSWORD"),
        'HOST': os.getenv(f"{ENV_VARS_SETTINGS_PREFIX}DATABASE_HOST"),
        'PORT': os.getenv(f"{ENV_VARS_SETTINGS_PREFIX}DATABASE_PORT"),
    }
}
