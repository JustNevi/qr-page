DEBUG = False
SECRET_KEY = os.getenv(f"{ENV_VARS_SETTINGS_PREFIX}SECRET_KEY")


# Enable corsheaders
INSTALLED_APPS.append("corsheaders")

ALLOWED_HOSTS = os.getenv(f"{ENV_VARS_SETTINGS_PREFIX}ALLOWED_HOSTS").split(',')
ALLOWED_HOSTS = [host.strip() for host in ALLOWED_HOSTS if host.strip()]

CORS_ALLOWED_ORIGINS = os.getenv(f"{ENV_VARS_SETTINGS_PREFIX}CORS_ALLOWED_ORIGINS").split(',')
CORS_ALLOWED_ORIGINS = [host.strip() for host in CORS_ALLOWED_ORIGINS if host.strip()]

# Put CorsMiddleware before CommonMiddleware
common_middleware_index = MIDDLEWARE.index("django.middleware.common.CommonMiddleware")
MIDDLEWARE.insert(common_middleware_index, "corsheaders.middleware.CorsMiddleware")


# MySQL configuration
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


# MinIO configuration
INSTALLED_APPS.append("minio_storage")

STORAGES = { 
    "default": {
        "BACKEND": "minio_storage.storage.MinioMediaStorage",
    },
    "staticfiles": { 
        "BACKEND": "minio_storage.storage.MinioStaticStorage",
     },
}

MINIO_STORAGE_ENDPOINT = os.getenv(f"{ENV_VARS_SETTINGS_PREFIX}MINIO_ENDPOINT")
MINIO_STORAGE_ACCESS_KEY = os.getenv(f"{ENV_VARS_SETTINGS_PREFIX}MINIO_ACCESS_KEY")
MINIO_STORAGE_SECRET_KEY = os.getenv(f"{ENV_VARS_SETTINGS_PREFIX}MINIO_SECRET_KEY")

MINIO_STORAGE_MEDIA_BUCKET_NAME = 'local-media'
MINIO_STORAGE_AUTO_CREATE_MEDIA_BUCKET = True
MINIO_STORAGE_STATIC_BUCKET_NAME = 'local-static'
MINIO_STORAGE_AUTO_CREATE_STATIC_BUCKET = True

MINIO_STORAGE_MEDIA_BACKUP_BUCKET = 'Recycle Bin'
MINIO_STORAGE_MEDIA_BACKUP_FORMAT = '%c/'

MINIO_STORAGE_USE_HTTPS = False
MINIO_STORAGE_MEDIA_OBJECT_METADATA = {"Cache-Control": "max-age=1000"}
