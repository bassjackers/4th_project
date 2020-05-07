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
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': db_info.get('db_name'),
        'PASSWORD': db_info.fet('db_password'),
        'USER': db_info.get('db_user'),
        'HOST': db_info.get('db_host'),
        'PORt': db_info.get('db_port'),
    }
}

DEBUG = True

INSTALLED_APPS += ['debug_toolbar']