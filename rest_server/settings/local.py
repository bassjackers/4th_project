from .base import * 

import json
import os

filename = 'settings/db_info_local.json'

db_file =  os.path.join(BASE_DIR, filename)


with open(db_file, 'r') as f:
    
    data = f.read()
    db_info = json.loads(data)

    


DATABASES = {
    # local용 DB Info
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': db_info.get('db_name'),
        'PASSWORD': db_info.get('db_password'),
        'USER': db_info.get('db_user'),
        'HOST': db_info.get('db_host'),
        'PORt': db_info.get('db_port'),
    }
}

DEBUG = True

INSTALLED_APPS += ['debug_toolbar']

MIDDLEWARE += ['debug_toolbar.middleware.DebugToolbarMiddleware',]
INTERNAL_IPS = [
    '127.0.0.1',
    'localhost'
]