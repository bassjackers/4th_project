from .base import * 

DATABASES = {
    # local용 DB Info
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

DEBUG = True

INSTALLED_APPS += ['debug_toolbar']