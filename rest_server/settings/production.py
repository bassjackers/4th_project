from .base import * 

DATABASES = {
    # production DB Info
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = False

ALLOWED_HOSTS = [
    '0.0.0.0'
]
