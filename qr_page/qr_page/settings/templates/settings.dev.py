DEBUG = True
SECRET_KEY = 'django-insecure-gdwlh_(gw&qhe6pncghs!s_z8f)!58kj_s&2d(h1@9@0@8&m$l'

# Enable corsheaders for local tests

LOCALHOST_PORT = 5173

INSTALLED_APPS.append("corsheaders")

CORS_ALLOWED_ORIGINS = [f"http://localhost:{LOCALHOST_PORT}"]

# Put CorsMiddleware before CommonMiddleware
common_middleware_index = MIDDLEWARE.index("django.middleware.common.CommonMiddleware")
MIDDLEWARE.insert(common_middleware_index, "corsheaders.middleware.CorsMiddleware")
