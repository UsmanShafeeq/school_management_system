# settings/development.py

from .base import *

DEBUG = True  # Debugging enabled in development

# Localhost and local IPs allowed
ALLOWED_HOSTS = ['localhost', '127.0.0.1']

# Development database (SQLite is sufficient here)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'dev_db.sqlite3'),
    }
}

# Static files
STATIC_URL = '/static/'

# You can also configure email settings or any development-specific configuration here
