import os

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'mammoth',
        'USER': 'mammoth',
        'PASSWORD': 'mammoth',
        'HOST': 'db',
        'PORT': 5432,
    }
}

DJANGO_PATH = "/usr/src/mammoth"
