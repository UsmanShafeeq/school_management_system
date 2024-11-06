# settings/production.py

from .base import *

DEBUG = False  # Disable debugging in production

# Set ALLOWED_HOSTS to your domain or production IP addresses
ALLOWED_HOSTS = ['yourdomain.com', 'www.yourdomain.com', 'your-server-ip']

# Production database (using PostgreSQL or MySQL is recommended for production)
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_db_name',
        'USER': 'your_db_user',
        'PASSWORD': 'your_db_password',
        'HOST': 'localhost',  # Use your production DB server
        'PORT': '5432',       # Default PostgreSQL port
    }
}

# Enable secure cookies in production
CSRF_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True

# Use a proper logging system (like Sentry or others) for production error monitoring
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'level': 'ERROR',
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': True,
        },
    },
}

# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')  # Directory to collect static files for production

# You can add other production-specific settings such as caching, email, and more
